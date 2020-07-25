import db_conn
import db_queries as queries
import bcolors
import math
import datetime as dt
import matplotlib.pyplot as plt

# Start Global Section *******************************************
db = db_conn.DB_Conn()
cnx = db.connect2shoppingdb()
q = queries.DB_Queries()
# End Global Section *********************************************


def task_selection():
    selection = 0
    tasks = {
        0:'Capture a Weight Measurement.',
        1:'Visualize Trend.',
        2:'Update height.',
        3:'Exit.'
    }

    print("Where do you want to go today?\n")
    for task_id, task_desc in tasks.items():
        print("\t[", task_id, "] ", task_desc)

    try:
        selection = int(input("\tYour selection: "))
        return selection
    except ValueError:
        print("[ERROR] Your selection is incorrect!")
        return 3 # Return exit code


def print_header():
    print("************************************************")
    print(f"{bcolors.bcolors.OKBLUE}*  Welcome to the Weight Manager Application!  *{bcolors.bcolors.ENDC}")
    print("************************************************")
    print()


def get_current_height(cnx):
    current_height = q.db_current_height(cnx=cnx)
    #print(current_height)
    return current_height


def capture_weight_measurement():
    flag = True
    while flag == True:
        print("What is your weight today? Don't be shy!")
        try:
            weight = float(input("Weight:"))
            flag = False
        except ValueError:
            print("[ERROR] The weight value is incorrect!")
            flag = True
    return weight


def calculate_bmi(weight, height):
    bmi = weight/math.pow(height, 2)
    print("Your BMI for your current weight and height is: {b:2.2f}".format(b=bmi))
    return bmi


def save_weight_data(weight, bmi):
    today_date = dt.date.today()
    id = q.save_weight_data_2db(today_date=today_date, weight=weight, bmi=bmi, cnx=cnx)
    print("Saved?", id)


def visualize_weight_his(y):
    n = len(y)
    x = list(range(n))
    plt.plot(x, y, 'go--', linewidth=2, markersize=12)
    for a, b in zip(x, y):
        plt.text(a, b, str(b))
    plt.title("Your weight trend! Keep up the hard work!")
    plt.xlabel("Measurements")
    plt.ylabel("Weight (Kg)")
    plt.show()


def main():
    print("\n")
    print_header()
    current_height = get_current_height(cnx)
    print("Current height is:", current_height)
    task = task_selection()

    if task == 0:
        weight = capture_weight_measurement()
        bmi = calculate_bmi(weight, current_height)
        save_weight_data(weight, bmi)
    elif task == 1:
        weights = q.get_weight_his(cnx=cnx)
        visualize_weight_his(weights)

    # Closing DB connecttion
    cnx.close()


if __name__ == "__main__":
    main()