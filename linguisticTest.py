import main_fuzzy as lin

lin.add_new_pattern("wzrost",{
    "bardzoniski": {"function": "triangle", "a": 80,"b": 110,"c": 135},
    "niski": {"function": "triangle", "a": 130,"b": 155,"c": 165},
    "wysoki": {"function": "triangle", "a": 160,"b": 180,"c": 190},
    "gigant": {"function": "triangle", "a": 180,"b": 200,"c": 220}
})
print("Available patterns - ",lin.get_patterns_names())

res = lin.value_is("wzrost","niski",170)
print("170 is wysoki?",res)

res = lin.one_to_lingustic("wzrost",170)
print("170 is ",res)

res = lin.list_to_lingustic("wzrost",[170, 110])
print("170 and 110 are - ",res)

lin.add_new_pattern("wiek",{
    "mlody":{"function": "triangle", "a":10,"b":15,"c":30}, 
    "stary": {"function": "triangle", "a":25,"b":45,"c":55}
    })
print("Available patterns - ",lin.get_patterns_names())

res = lin.one_to_lingustic("wiek",11, 0.1)
print("11 is",res)