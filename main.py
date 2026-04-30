import core.parser as parser
import core.differentiator as differentiator
import core.integrator as integrator
import core.plotter as plotter

def main():
    print("=== Calculus Graphing App ===\n")

    user = input("Enter a function f(x): ")

    while True:
        print(f"\nFunction: \n{parser.parse_function(user)}")

        print("\nWhat do you want to do?")
        print("[1] Evaluate f(x), f'(x) at a point")
        print("[2] Compute definite integral between two bounds")
        print("[3] Plot f(x), f'(x), and ∫f(x)dx")
        print("[4] Show symbolic derivative and integral")
        print("[5] Enter new function")
        print("[6] Exit")

        choice = input("\nChoice: ").strip()

        if choice == '1':
            x_val = float(input("Enter x-value: "))
            print(f"\nf({x_val})  = {parser.parse_function(user, x_val, True)}")
            print(f"f'({x_val}) = {differentiator.differentiate(user, x_val, True)}")

        elif choice == '2':
            a = float(input("Enter lower bound: "))
            b = float(input("Enter upper bound: "))
            print(f"\n∫f(x)dx from {a} to {b} = {integrator.integration(user, a, b, True)}")

        elif choice == '3':
            plotter.plot(user)

        elif choice == '4':
            print(f"\nDerivative : {differentiator.differentiate(user)}")
            print(f"Integral   : \n{integrator.integration(user)}")
        
        elif choice == '5':
            user = input("Enter a function f(x): ")

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")

main()