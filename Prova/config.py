import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Assigna els valors des del fitxer de configuració
posibles_moviments = config['Configuracio']['posibles_moviments'].split(',')
reward_prohibit = float(config['Configuracio']['reward_prohibit'])
reward_fora = float(config['Configuracio']['reward_fora'])
reward_blank = float(config['Configuracio']['reward_blank'])
reward_final = float(config['Configuracio']['reward_final'])
# reward_inici = float(config['Configuracio']['reward_inici'])
max_prohibits = int(config['Prohibicions']['max_prohibits'])
casella_prohibit = tuple(map(int, config['Prohibicions']['casella_prohibit'].split(',')))
gamma = float(config["Configuracio"]["gamma"])
mareig = int(config['Configuracio']['mareig'])
tamany_graella = list(map(int, config['tamany_graella']['dimensions'].split(',')))
policy_file = config['Configuracio']['policy_file']

def llegir_policies():
    try:
        with open(f'policies/{policy_file}', 'r') as file:
            policies_data = file.readlines()
        policies = []
        for line in policies_data:
            cell, policy_with_prob = line.strip().split('=')
            cell = eval(cell)  # Converteix la cadena "(x, y)" en una tupla (x, y)
            policy_probs = {policy: float(prob) for policy, prob in (p.split(':') for p in policy_with_prob.split())}
            policies.append((cell, policy_probs))
    except Exception as e:
            print(f"¡¡¡¡¡¡¡¡¡¡ERROR DE FORMAT!!!!!!!!!!!!! a {policy_file}, esborra files buides o revisa typos.")
            print(e)
    return policies
