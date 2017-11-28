from util import *
from parser import *

def remove_implication(e):
	if isinstance(e, tuple):
		op = e[0]
		if op == '=>':
			_, antecedent, consequent = e
			x = remove_implication (('not', antecedent))
			y = remove_implication (consequent)
			return ('or', x, y)
		else:
			return argmap(e[0], remove_implication, e)
	else:
		return e		

def move_not_in (e):
	if not isinstance(e, tuple):
		return e
	else:
		op = e[0]
		if op != 'not':
			return argmap (op, move_not_in, e)
		else:	
			_, e = e
			if isinstance(e, tuple):
				op = e[0]
				if op == 'or':
					_, a, b = e
					x = 'and'
					y = move_not_in (('not', a))
					w = move_not_in (('not', b))
					z = (x, y, w)
					return z
				elif op == 'not':
					_, e = e
					nxt = move_not_in(e)
					return nxt
				elif op == 'There_exists':
					op, var, e = e
					nxt = move_not_in (('not', e))
					z = ('For_every', var, nxt)
					return z
				elif op == 'and':
					_, a, b = e
					x = 'or'
					y = move_not_in (('not', a))
					w = move_not_in (('not', b))
					z = (x, y, w)
					return z
				elif op == 'For_every':
					op, var, e = e
					nxt = move_not_in (('not', e))
					z = ('There_exists', var, nxt)
					return z
				else:
					return ('not', argmap(op, move_not_in, e))
			else:
				return ('not', e)

def binding(name, env):
	if env is None:
		raise VariableError(name)
	else:
		while env is not None:
			(variable, value), env = env
			if name == variable:
				return value		

def skolemize(e, env = None):
	if isinstance(e, tuple):
		op = e[0]
		if op == 'For_every':
			_, var, e = e
			env = ((var, ('forall', var)), env)
			x = op
			y = var
			z = skolemize(e, env)
			return (x, y, z)
		elif op == 'There_exists':
			bound = []
			varb = env
			while varb is not None:
				(variable, value), varb	= varb
				if value[0] is 'forall':
					bound.append(variable)

			stoken = 'ST{}'.format(scounter.next())
			if len(bound) > 0:
				salready = (stoken,)
				balready = tuple(bound)
				stoken = salready + balready

			_, variable, e = e
			env = ((variable, ('There_exists', stoken)), env)
			return skolemize(e, env)
		else:
			return argmap(op, lambda y: skolemize(y, env), e)
	elif isinstance(e, str) and e[0] == e[0].lower():
		typ, value = binding(e, env)
		return value
	else:
		return e								

def remove_quantifiers(e):
	if not isinstance(e, tuple):
		return e
	else:
		operator = e[0]
		if operator == 'For_every':
			return remove_quantifiers(e[2])
		else:
			return argmap(operator, remove_quantifiers, e)

def distribute_and_over_or(e):
	def G(e):
		if isinstance(e, tuple) and e[0] == 'or':
			_, a, b = e
			a, b = G(a), G(b)
			if isinstance(a, tuple) and a[0] == 'and':
				_, c, d = a
				x = G(('or', c, b))
				y = G(('or', d, b))
				z = ('and', x, y)
				return z
			elif isinstance(b, tuple) and b[0] == 'and':
				_, c, d = b
				x = G(('or', c, a))
				y = G(('or', d, a))
				z = ('and', x, y)
				return z
			else:
				return ('or', a, b)
		elif isinstance(e, tuple):
			return argmap(e[0], G, e)
		else:
			return e
	return G(e)

def alter(e):
	if isinstance(e, tuple):
		temp = ('and', 'or')
		if e[0] in temp:
			operator, e1, e2 = e
			e1 = alter(e1)
			e2 = alter(e2)
			if isinstance(e1, tuple) and e1[0] is operator:
				r = e1[1:]
			else:
				r = (e1,)

			if isinstance(e2, tuple) and e2[0] is operator:
				r += e2[1:]
			else:
				r += (e2,)

			return (operator,) + r
		else:
			return argmap(e[0], alter, e)
	else:
		return e									

def infix (e):
    if isinstance (e, tuple):
        op = e[0]
        operators = ('and', 'or')
        if op in operators:
        	if op == 'and':
        		op = ' & '
        	else:
        		op = ' | '
        	z = op.join ([infix (x) for x in e[1:]])	
        	return '(' + z + ')'
        elif op == 'not':
            return '~{}'.format(infix (e[1]))
        else:
        	z = [infix(x) for x in e[1:]]
        	return '{}({})' .format(op, ', '.join (z))
    else:
        return '{}'.format(e)

def cnf(e):
	e = remove_implication(e)
	e = move_not_in(e)
	e = skolemize(e)
	e = remove_quantifiers(e)
	e = distribute_and_over_or (e)
	e = alter(e)
	return e        


def main():
	r = ['rules1.txt', 'rules2.txt', 'rules3.txt', 'rules4.txt']
	w = ['kb1.txt', 'kb2.txt', 'kb3.txt', 'kb4.txt']

	for i in range(0, 4):
		rd = open(r[i], 'r')
		wr = open(w[i], 'w')
		line = rd.readline()
		while line:
			st = parse_string(line)
			wr.write(infix(cnf(st)) + "\n")
			line = rd.readline()
		rd.close()
		wr.close()	
          
if __name__ == "__main__":
    main()