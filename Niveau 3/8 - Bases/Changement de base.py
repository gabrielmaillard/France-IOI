source_base, final_base, num_Figures = map( int, input().split() )
num_decimal = 0
figures = map( int, input().split() )
for figure in figures:
   num_decimal = (num_decimal * source_base) + figure
def print_(number,num_figures):
   if number >= final_base:
      print_(number // final_base, num_figures + 1)
   print(number % final_base,end=" ")
      
print_(num_decimal,1)