
from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z, salary, tax_rate, tax_rate_for_salary_above, net_salary')

salary['foo'] = 60
salary['bar'] = 110

print(salary[X]==Y)

salary['foo']==Y

# give me all the X that have a salary of 110
print(salary[X]==110)

# not Y?
print((salary[X]==Y) & ~(Y==110))


+(tax_rate[None]==0.33)
# give me the net salary for all X
print((Z==salary[X]*(1-tax_rate[None])))





pyDatalog.create_atoms('factorial, N, F') # gives datalog capability to these words

def run_program():

    N = pyDatalog.Variable()
    F = pyDatalog.Variable()
    file_in = open("sample_datalog_program.dl", 'r')
    mc = file_in.read()
    print mc
    @pyDatalog.program()
    def _(): # the function name is ignored
        pyDatalog.load(mc)
        #pyDatalog.load("""
        #+ (factorial[1]==1)
        #(factorial[N] == F) <= (N > 1) & (F == N*factorial[N-1])
        #""")
        print(pyDatalog.ask('factorial[4]==F'))
    file_in.close()
    pass


# if __name__ == "__main__":
    # run_program()
