
def is_correct():
    layer = [tree[0]]

    while layer:
        next_layer = []

        for node in layer:
            if 'max' in node and node['value'] >= node['max']:
                return False

            if 'min' in node and node['value'] < node['min']:
                return False

            if node['left'] > -1:
                next_layer.append(tree[node['left']])
                next_layer[-1]['max'] = node['value']

                if 'min' in node:
                    next_layer[-1]['min'] = node['min']

            if node['right'] > -1:
                next_layer.append(tree[node['right']])
                next_layer[-1]['min'] = node['value']
                if 'max' in node:
                    next_layer[-1]['max'] = node['max']
        layer = next_layer

    return True

n = int(input())

if n <= 1:
    print('CORRECT')
else:
    tree = [{} for i in range(n)]
    for i in range(n):
        v, l, r = [int(s) for s in input().split()]
        tree[i]['value'] = v
        tree[i]['right'] = r
        tree[i]['left'] = l
    if is_correct():
        print('CORRECT')
    else:
        print('INCORRECT')
