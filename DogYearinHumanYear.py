class DogCare:
    percentageOfDogsWeight = 2.5
    dogsAge = [[15,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80],
               [15,24,28,32,36,42,47,51,56,60,65,69,74,78,83,87],
               [15,24,28,32,36,45,50,55,61,66,72,77,82,88,93,120]]

    def dog_food(dog_kg):
        return (dog_kg * DogCare.percentageOfDogsWeight) / 100


    def dog_age(dog_age_in_human_years, dog_kg):
        if dog_kg < 7:
            return DogCare.dogsAge[0][dog_age_in_human_years-1]
        elif dog_kg < 17:
            return DogCare.dogsAge[1][dog_age_in_human_years-1]
        else:
            return DogCare.dogsAge[2][dog_age_in_human_years-1]

    def dog_exercise(dog_age_in_human_years, dog_kg):
        if DogCare.dog_age(dog_age_in_human_years,dog_kg) < 15:
            return "15 Min of exercise"
        elif DogCare.dog_age(dog_age_in_human_years,dog_kg) < 75:
            return "75 Min of exercise"
        else:
            return "30 Min of exercise"



print(DogCare.dog_food(5))
print(DogCare.dog_age(7,90))
print(DogCare.dog_exercise(5,70))

