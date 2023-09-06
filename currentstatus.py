
class Status():
    def __init__(self, blood_preasure, temperature, o2sat, respiratory_rate, score):

        self.blood_preasure = blood_preasure
        self.temperature = temperature
        self.o2sat = o2sat
        self.respiratory_rate = respiratory_rate
        self.score = score

    @staticmethod
    def newstatus():
        print("\n --- VITAL SIGNS ---\n")

        blood_preasure = int(input("Enter the blood preasure: "))
        temperature = float(input("Enter the temperature in C: "))
        o2sat = int(input("Enter the o2sat %: "))
        respiratory_rate = int(input("Enter the respiratory rate: "))

        # Implementation of a medical score, for each value out of range, the score increases by 1 and if the score is greater than 2, the patient is in critical condition
        # then it with be sent to a bed and a doctor will be notified to atend it inmediately.
        score = 0

        if (blood_preasure > 140) or (blood_preasure < 90):
            score = score + 1
        if (temperature > 37.5) or (temperature < 36):
            score = score + 1
        if (o2sat < 95) or (o2sat > 100):
            score = score + 1
        if (respiratory_rate > 25) or (respiratory_rate < 12):
            score = score + 1
        print("Score: ", score)
        if (score <= 2):
            print("The patient is in regular condition and don't need a bed inmediately")
        if (score > 2):
            print("The patient is in critical condition and will be put in bed inmediately if there is one available")

        recentstatus = Status(blood_preasure, temperature,
                              o2sat, respiratory_rate, score)
        return recentstatus
