from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):

	results = [hypothesis]

	for rule in rules:
		consequent = rule.consequent()

		for expr in consequent:
			bindings = match(expr, hypothesis)

			if bindings or expr == hypothesis:
				antecedent = rule.antecedent()

				if isinstance(antecedent, str):
					new_hypothesis = populate(expr, bindings)
					results.append( backchain_to_goal_tree(rules, new_hypothesis) )
					results.append(new_hypothesis)
				else:
					statements = [populate(expr, bindings) for ante_expr in antecedent]
					new_results = []
					for statement in statements:
						new_results.append( backchain_to_goal_tree(rules, statement) )
					results.append(create_statement(new_results, antecedent))
	return simplify(results)








	# 	actors = match( c_rule.consequent()[0], hypothesis)	
		
	# 	if (actors is None):
	# 		continue

	# 	if ( populate(c_rule.consequent()[0], actors) == hypothesis ):
	#  		if ( isinstance(c_rule.antecedent, (list, OR, AND) ) ):
	#  		 	rules.append( AND( populate(c_rule.antecedent(), actors) ) )
	#  		else:
	#  		 	rules.append( AND( populate(c_rule.antecedent(), actors) )  )

	# for rule in or_to_check:
	# 	simplify(rule)

	# rules = simplify(rules)

	# for rule in rules:
	# 	try:
	# 		backchain_to_goal_tree(rules, hypothesis)
	# 	except:
	# 		pass

	# print
	# print
	# print
	# print simplify(rules)
	# print
	# # return or_to_check.simplify
	# pass



def create_statement(statements, rule):
    if isinstance(rule, AND):
        return AND(statements)
    elif isinstance(rule, OR):
        return OR(statements)


# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
