#Finding out the number of machines
#machine_no can be similarly made a parameter
machine_no = int(input())
machine_dict = {}
machine_count = 1
for i in range(machine_no):
     machine_dict["machine"+str(machine_count)] = {}
     machine_count += 1 

machine_count = 1


#Finding out number of wheels per machine and the periodicity of each
if machine_no <= 100:
    wheel_count = 1
    for i in range(machine_no):
         wheel_number = int(input())
         machine_dict["machine"+str(machine_count)] = list(map(int, input().split()))
         machine_count += 1
    

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

machine_count = 1

lcm = 1
for i in machine_dict:
    for i in machine_dict["machine"+str(machine_count)]:
      lcm = lcm * i//gcd(lcm, i)
    if lcm <= 10 ** 9:
        print(lcm) 
    else:
        print("More than a billion.")
    lcm = 1
    machine_count += 1
     
