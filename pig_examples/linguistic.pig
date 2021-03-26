REGISTER 'myudf.py' using jython as myudfs
REGISTER './main_fuzzy.py' using jython as fuzzy
 
users = LOAD 'user_data' USING PigStorage(',') AS (firstname: chararray, lastname:chararray,wzrost:int, wiek:int);
DUMP users;
-- (zosia,samosia,150,12)
-- (ala,makota,170,32)
-- (harry,potter,144,89)
-- (ola,makota,175,8)
fuzzy_users = FOREACH users GENERATE firstname, lastname, wzrost, fuzzy.one_to_lingustic('wzrost', wzrost,0.3) as fuzzy_wzrost, wiek, fuzzy.one_to_lingustic('wiek', wiek,0.3) as fuzzy_wiek;
 
DUMP fuzzy_users;
-- (zosia,samosia,150,niski,12,mlody)
-- (ala,makota,170,wysoki,32,stary)
-- (harry,potter,144,niski,89,emeryt)
-- (ola,makota,175,wysoki,8,dzieciak)
grouped_fuzzy_users = GROUP fuzzy_users BY fuzzy_wzrost;
 
DUMP grouped_fuzzy_users;
-- (niski,{(harry,potter,144,niski,89,emeryt),(zosia,samosia,150,niski,12,mlody)})
-- (wysoki,{(ola,makota,175,wysoki,8,dzieciak),(ala,makota,170,wysoki,32,stary)})
 
users2 = LOAD 'user_data' USING PigStorage(',') AS (firstname: chararray, lastname:chararray,wzrost:int, wiek:int, zajecie:chararray);
fuzzy_us2 = FOREACH users GENERATE fuzzy.one_to_lingustic('wzrost', wzrost,0.3) as fw, zajecie;
 
self_joined_fuzzy_users = JOIN fuzzy_users BY fuzzy_wzrost, fuzzy_us2 BY fw;
 
DUMP self_joined_fuzzy_users;
-- (harry,potter,144,niski,89,emeryt,niski,nauczyciel)
-- (harry,potter,144,niski,89,emeryt,niski,uczen)
-- (zosia,samosia,150,niski,12,mlody,niski,nauczyciel)
-- (zosia,samosia,150,niski,12,mlody,niski,uczen)
-- (ola,makota,175,wysoki,8,dzieciak,wysoki,pacjent)
-- (ola,makota,175,wysoki,8,dzieciak,wysoki,prawnik)
-- (ala,makota,170,wysoki,32,stary,wysoki,pacjent)
-- (ala,makota,170,wysoki,32,stary,wysoki,prawnik)