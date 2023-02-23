import boto3

# Configuração das credenciais da AWS
aws_access_key_id = 'sua chave de acesso aqui'
aws_secret_access_key = 'sua chave secreta aqui'
region_name = 'sua região aqui'

# Criação da conexão com o serviço Elastic Load Balancing
elb_client = boto3.client('elbv2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Obtém todos os load balancers
load_balancers = elb_client.describe_load_balancers()['LoadBalancers']

# Loop em cada load balancer
for load_balancer in load_balancers:
    # Obtém o nome do load balancer
    load_balancer_name = load_balancer['LoadBalancerName']

    # Obtém os targets do load balancer
    target_groups = elb_client.describe_target_groups(LoadBalancerArn=load_balancer['LoadBalancerArn'])['TargetGroups']

    # Verifica se há targets no load balancer
    if target_groups:
        print(f'O load balancer {load_balancer_name} está em uso.')
    else:
        print(f'O load balancer {load_balancer_name} não está em uso.')
