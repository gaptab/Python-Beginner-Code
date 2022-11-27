import js2py
js_1='console.log("Running JavaScript in Python")'
res1=js2py.eval_js(js_1)

# JavaScript Function
x=int(input("Enter the value of x: "))
js_2='''function add(x,y){
    return x+y
    }'''
res2=js2py.eval_js(js_2)
print("Result: x+3=",res2(x,3))