from random import randint
import random
import json


class Step:
    def __init__(self, id, intent, expressions):
        self.id = id
        self.intent = intent
        self.expressions = expressions

    def id(self):
        return self.id

    def intent(self):
        return self.intent

    def random_expression(self):
        return self.expressions[randint(0, (len(self.expressions) - 1))]


class Node:

    def __init__(self, id, step, outgoing_steps):
        self.id = id
        self.step = step
        self.outgoing_steps = outgoing_steps

    def id(self):
        return self.id

    def step(self):
        return self.step

    def random_outgoing_step(self):
        return self.outgoing_steps[randint(0, (len(self.outgoing_steps) - 1))]


steps = {'start': Step('start', 'start', ['start']), 'end': Step('end', 'end', ['end'])}

with open('resources/buyer_steps_mp.json') as f:
    data = json.load(f)

for node in data:
    steps[node['id']] = Step(node['id'], node['intent'], node['expressions'])

with open('resources/seller_steps_mp.json') as f:
    data = json.load(f)

for node in data:
    steps[node['id']] = Step(node['id'], node['intent'], node['expressions'])

with open('resources/state_machine_mp.json') as f:
    data = json.load(f)

node_dict = {}

for node in data:
    node = Node(node['node_id'], node['step_id'], node['outgoing_nodes'])
    node_dict[node.id] = node

params1 = {
    'product_name1': 'bedsheet',
    'product_quantity1': 200 ,
    'product_name2': 'rug',
    'product_quantity2': 100,
    'delivery_location': 'Hyderabad',
    'buyer_product_price1': 700 ,
    'buyer_product_price2': 500 ,
    'seller_name': 'Ramesh Textiles',
    'seller_product_price1': 800,
    'seller_product_price2': 600,
    'seller_product_revised_price1': 750,
    'seller_product_revised_price2':  550,
    'discount':10,
    'seller_revised_discount': 10,
    'buyer_revised_discount': 15,
    'seller_additional_quantity_product_2': 50

}

params2 = {
    'product_name1': 'whiteboard',
    'product_quantity1': 60 ,
    'product_name2': 'marker',
    'product_quantity2': 500,
    'delivery_location': 'Kolkata',
    'buyer_product_price1': 500 ,
    'buyer_product_price2': 20 ,
    'seller_name': 'Krishna stationary',
    'seller_product_price1': 600,
    'seller_product_price2': 30,
    'seller_product_revised_price1':550,
    'seller_product_revised_price2':  25,
    'discount':5,
    'seller_revised_discount': 5,
    'buyer_revised_discount': 10,
    'seller_additional_quantity_product_2': 100

}

params3 = {
    'product_name1': 'apple',
    'product_quantity1': 300 ,
    'product_name2': 'orange',
    'product_quantity2': 400,
    'delivery_location': 'Chennai',
    'buyer_product_price1': 35 ,
    'buyer_product_price2': 25 ,
    'seller_name': 'Ram wholesale and retail',
    'seller_product_price1': 45,
    'seller_product_price2': 35,
    'seller_product_revised_price1': 40,
    'seller_product_revised_price2':  30,
    'discount':15,
    'seller_revised_discount': 15,
    'buyer_revised_discount': 20,
    'seller_additional_quantity_product_2': 50

}

params4 = {
    'product_name1': 'ruled book',
    'product_quantity1': 1000 ,
    'product_name2': 'plain book',
    'product_quantity2': 1500,
    'delivery_location': 'Mumbai',
    'buyer_product_price1': 30 ,
    'buyer_product_price2': 20 ,
    'seller_name': 'Krishna stationary',
    'seller_product_price1': 40,
    'seller_product_price2': 30,
    'seller_product_revised_price1': 35,
    'seller_product_revised_price2':  25,
    'discount':5,
    'seller_revised_discount': 5,
    'buyer_revised_discount': 10,
    'seller_additional_quantity_product_2': 250

}

params5 = {
    'product_name1': 'paper plate',
    'product_quantity1':  1000 ,
    'product_name2': 'plastic spoon',
    'product_quantity2': 1000,
    'delivery_location': 'delhi',
    'buyer_product_price1': 5 ,
    'buyer_product_price2': 3,
    'seller_name': 'Ramesh Retail',
    'seller_product_price1': 10,
    'seller_product_price2': 5,
    'seller_product_revised_price1': 7,
    'seller_product_revised_price2':  4,
    'discount':10,
    'seller_revised_discount': 10,
    'buyer_revised_discount': 15,
    'seller_additional_quantity_product_2': 200

}


params=[params1,params2,params3,params4,params5]
is_buyer=[]
for i in range(0, 1000):
    node = node_dict['start']
    print ('=======START============',file=open("output1.txt", "a"))
    params_used=random.choice(params)
    b=[]
    while node.id != 'end':
        
        expression = steps[node.step].random_expression()
        if node.id!= 'start':
            if (steps[node.step].id)[0]=='b':
                b.append(1)
            else:
                b.append(0)
        
        for key in params_used.keys():
            expression = expression.replace("{{" + key + "}}", str(params_used[key]))
        print (expression, file=open("output1.txt", "a"))
        node = node_dict[node.random_outgoing_step()]
        
    print (steps[node.step].random_expression(), file=open("output1.txt", "a"))
    print ('=======END============',file=open("output1.txt", "a"))
    is_buyer.append(b)
