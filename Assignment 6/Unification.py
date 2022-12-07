global no_of_pred
global predicate
global no_of_args 
global argument

predicate = []
no_of_args = []
argument = []
def main():
    ch = 'y'
    
    while ch=='y':
        print("=========PROGRAM FOR UNIFICATION=========")
        global predicate
        global no_of_pred
        # breakpoint()
        global no_of_args
        global argument
        no_of_pred = int(input("Enter number of predicates:- "))
        nouse = ""
        temp = list()
        for i in range(no_of_pred):
            nouse = input("")
            temp_v = input("Enter predicate "+str(i+1)+":- ")
            temp.append(temp_v)
            temp_i = int(input(f"Enter No.of Arguments for Predicate {temp_v}:- "))
            
            no_of_args.append(temp_i)
            arg_temp = []
            for j in range(temp_i):
                nouse = input("")
                t = input(f"Enter argument {j+1}: ")
                arg_temp.append(t)
            argument.append(arg_temp)
            predicate.append(temp)
        display()
        chk_arg_pred()
        ch = input("Do you want to continue(y/n):  ")
        predicate = []
        no_of_args = []
        argument = []
        no_of_pred = []

def display():
    global predicate
    global argument
    global no_of_args
    global no_of_pred
    print("\n\t=======PREDICATES ARE======")
    for i in range(no_of_pred):
        print(f"{predicate[i]}(")
        for j in range(no_of_args[i]):
            print(argument[i][j])
            if(j!=no_of_args[i]-1):
                print(",")
        print(")")

def chk_arg_pred():
    pred_flag = 0
    arg_flag = 0
    global no_of_args
    global predicate
    global no_of_pred
    for i in range(no_of_pred-1):
        if predicate[i]!=predicate[i+1]:
            print("\nPredicates are not same..")
            print("\nUnification cannot progress!")
            pred_flag = 1
            break
    if(pred_flag!=1):
        for i in range(no_of_args[i]-1):
            if(no_of_args[i]!=no_of_args[i+1]):
                print("\nArguments Not Same..!")
                arg_flag = 1
                break;
        if(arg_flag==0 and pred_flag!=1):
            unify()

def unify():
    flag =0
    global no_of_pred
    global no_of_args
    global argument
    for i in range(no_of_pred-1):
        for j in range(no_of_args[i]):
            if(argument[i][j]!=argument[i+1][j]):
                if(flag==0):
                    print("\n\t======SUBSTITUTION IS======")
                print(f"\n\t{argument[i+1][j]}/{argument[i][j]}")
                flag+=1
    if(flag==0):
        print("\nArguments are identical...\nNo need of Substitution")

if __name__ == "__main__":
    main()
