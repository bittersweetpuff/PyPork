/*
* Example Pig script
* Adjust path to main_fuzzy.py and then you can run the script.
* To run this script use command: pig -x local linguistic.pig.
*/

REGISTER '/home/piggy/PyPork/main_fuzzy.py' using jython as fuzzy
--Ładowanie danych z pliku user_data: 
users = LOAD 'user_data.csv' USING PigStorage(',') AS (firstname: chararray, lastname:chararray,wzrost:int, wiek:int);
DUMP users;
-- (zosia,samosia,150,12)
-- (ala,makota,160,32)
-- (ALICJA,makota,160,18)
-- (harry,potter,194,89)
-- (ola,makota,175,8)

--Zamiana wartości na zmienną lingwistyczną(one_to_lingustic) wraz z wyliczeniem stopnia zgodnośći(fuzzy_level)
fuzzy_users = FOREACH users GENERATE firstname, lastname, wzrost, fuzzy.one_to_lingustic('wzrost', wzrost) as fuzzy_wzrost, fuzzy.fuzzy_level('wzrost',wzrost,fuzzy.one_to_lingustic('wzrost', wzrost)) as level, wiek, fuzzy.one_to_lingustic('wiek', wiek) as fuzzy_wiek;

DUMP fuzzy_users;
-- (zosia,samosia,150,niski,12,mlody)
-- (ala,makota,160,niski,32,stary)
-- (ALICJA,makota,160,niski,18,mlody)
-- (harry,potter,194,gigant,89,emeryt)
-- (ola,makota,175,wysoki,8,dzieciak)

--Groupowanie danych po zmiennej lingwistycznej:
grouped_fuzzy_users = GROUP users BY fuzzy.one_to_lingustic('wzrost', wzrost) ;

DUMP grouped_fuzzy_users;
-- (niski,{(ALICJA,makota,160,niski,18,mlody),(ala,makota,160,niski,32,stary),(zosia,samosia,150,niski,12,mlody)})
-- (gigant,{(harry,potter,194,gigant,89,emeryt)})
-- (wysoki,{(ola,makota,175,wysoki,8,dzieciak)})

users2 = LOAD 'user_data.csv' USING PigStorage(',') AS (firstname: chararray, lastname:chararray,wzrost:int, wiek:int, zajecie:chararray);
fuzzy_us2 = FOREACH users2 GENERATE fuzzy.one_to_lingustic('wzrost', wzrost) as fw, zajecie;

--złączenie dwóch PigStorage po zmiennej lingwistycznej
-- oba join daja ten sam wynik
-- self_joined_fuzzy_users = JOIN fuzzy_users BY fuzzy_wzrost, fuzzy_us2 BY fw;
self_joined_fuzzy_users = JOIN users BY fuzzy.one_to_lingustic('wzrost', wzrost), users2 BY fuzzy.one_to_lingustic('wzrost', wzrost);

DUMP self_joined_fuzzy_users;
-- (ALICJA,makota,160,niski,18,mlody,niski,prawnik)
-- (ALICJA,makota,160,niski,18,mlody,niski,prawnik)
-- (ALICJA,makota,160,niski,18,mlody,niski,uczen)
-- (ala,makota,160,niski,32,stary,niski,prawnik)
-- (ala,makota,160,niski,32,stary,niski,prawnik)
-- (ala,makota,160,niski,32,stary,niski,uczen)
-- (zosia,samosia,150,niski,12,mlody,niski,prawnik)
-- (zosia,samosia,150,niski,12,mlody,niski,prawnik)
-- (zosia,samosia,150,niski,12,mlody,niski,uczen)
-- (harry,potter,194,gigant,89,emeryt,gigant,nauczyciel)
-- (ola,makota,175,wysoki,8,dzieciak,wysoki,pacjent)

--Funkcja fuzzy_level wylicza stopień zgodności dla podanej wartości do zmiennej lingwistycznej wywołując odpowiednią funkcję przynależności.
filtered = FILTER users BY fuzzy.fuzzy_level('wzrost',wzrost,'wysoki') > 0.5;

DUMP filtered;
-- (ola,makota,175,8)

Przykłady łączenia funkcji za pomocą F_AND, F_OR i F_NOT. 

filtered_fand = FILTER users2 BY fuzzy.F_AND(fuzzy.triangle_membership(wzrost, 140.0, 150.0, 160.0), fuzzy.trapezoid_membership(wiek,10.0,12.0,20.0,30.0)) > 0.5;

DUMP filtered_fand;
-- -- (zosia,samosia,150,12,uczen)

filtered_for = FILTER users2 BY fuzzy.F_OR(fuzzy.triangle_membership(wzrost, 140.0, 150.0, 160.0), fuzzy.trapezoid_membership(wiek,10.0,12.0,20.0,30.0)) > 0.5;

DUMP filtered_for;
-- (zosia,samosia,150,12,uczen)
-- (ALICJA,makota,160,18,prawnik)

filtered_font = FILTER users2 BY fuzzy.F_NOT(fuzzy.trapezoid_membership(wiek,10.0,12.0,20.0,30.0)) > 0.5;

DUMP filtered_font;
-- (ala,makota,160,32,prawnik)
-- (harry,potter,194,89,nauczyciel)
-- (ola,makota,175,8,pacjent)

filtered_fand2 = FILTER users BY fuzzy.F_AND(fuzzy.fuzzy_level('wzrost',wzrost,'wysoki'), fuzzy.fuzzy_level('wiek',wiek,'dzieciak')) > 0.1;

DUMP filtered_fand2;
-- (ola,makota,175,8)

filtered_for2 = FILTER users BY fuzzy.F_OR(fuzzy.fuzzy_level('wzrost',wzrost,'wysoki'), fuzzy.fuzzy_level('wiek',wiek,'emeryt')) > 0.5;

DUMP filtered_for2;
-- (harry,potter,194,89)
-- (ola,makota,175,8)

--  Funkcja fuzzy.*_membership realizuje założenie funkcji około, gdyż zwraca stopień zgodności dla podanej funkcji przynależności. 
Przykładem takiego filtrowania byłoby wywołanie " fuzzy.*_membership(zmienna, parametry) > minimalne_ktyterium_zgodności). Poniżej przykład dla funkcji trójkątnej:

tmp = FILTER users2 BY fuzzy.triangle_membership(wzrost, 140.0, 150.0, 160.0) >0.5;
DUMP tmp;
-- (zosia,samosia,150,12,uczen)  

-- Funkcja fequal zwraca stopien zgodności obliczając punkty przecięcia rozmytych wartości.
-- Ze względu na ograniczenia Pig Latin dotyczące wywoływania udf(user defined functions) poprawne jej wykorzystanie do implementacji funkcji fjoin wydaje się niemożliwe.
tmp = FOREACH users2 GENERATE firstname, fuzzy.fequal(wzrost, 10, wzrost+5, 5);
DUMP tmp;
-- (zosia,0.6666666666666667)
-- (ala,0.6666666666666667)
-- (ALICJA,0.6666666666666667)
-- (harry,0.6666666666666667)
-- (ola,0.6666666666666667)   
