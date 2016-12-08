"""
Brian Hunscher
Created: 12/8/2016
Test here 
Test2
"""


import argparse

def monthlyPayment(LoanAmount, InterestRate, LengthYrs):
  L= float(LoanAmount)
  c= float(InterestRate)/12
  n= float(LengthYrs)*12

  P=L*(c*(1+c)**n)/((1+c)**n-1)
  Total = P*n
  TotalInterest = Total - L

  print("Monthly Payment: %f" % P)
  print("Total Loan Amount:%f" % Total)
  print("Total Interest Paid:%f" % TotalInterest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mortgage Calculator")
    parser.add_argument("LoanAmount", help="Loan Amount")
    parser.add_argument("InterestRate", help="Interest Rate (1% writen 0.01)")
    parser.add_argument("LengthYrs", help="Loan Length in years")

    args= parser.parse_args()
    monthlyPayment(args.LoanAmount, args.InterestRate, args.LengthYrs)
