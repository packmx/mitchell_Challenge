
# taking two inputs at a time 
var1, var2, var3, var4 = [int(x) for x in input("Enter a 4 values: ").split()]

var1_var2=complex(var1, var2)
var3_var4=complex(var3, var4)

add_vars= var1_var2 + var3_var4
sub_vars= var1_var2 - var3_var4
mul_vars= var1_var2 * var3_var4
div_vars= var1_var2 / var3_var4
print('Adding Complex numbers {0.real:.2f}  {0.imag:.2f}i'.format(add_vars))
print('Subtracting Complex numbers {0.real:.2f}  {0.imag:.2f}i'.format(sub_vars))
print('Multiplying Complex numbers {0.real:.2f}  {0.imag:.2f}i'.format(mul_vars))
print('Division Complex Numbers {0.real:.2f}  {0.imag:.2f}i'.format(div_vars))


mod_var1_var2 = abs(var1_var2)
print('Mod first 2 values {0.real:.2f}  {0.imag:.2f}i'.format(mod_var1_var2))
mod_var3_var4 = abs(var3_var4)
print('Mod second 2 values {0.real:.2f}  {0.imag:.2f}i'.format(mod_var3_var4))