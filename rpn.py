#!/usr/bin/env puthon3
import operator

ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv	
}

def calculate(myarg):
	stack = list() 
	for token in myarg.split():
		try:
			stack.append(int(token))
		except ValueError: 
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			function(arg1,arg2)
			result = function(arg1,arg2)
			stack.append(result)		
	#print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()


