def is_criticality_balanced(temperature, neutrons_emitted):
    '''

    :param temperature: int
    :param neutrons_emitted: int
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    '''

    if temperature < 800 and neutrons_emitted > 500:
        if temperature * neutrons_emitted < 500000:
            return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    '''

    :param voltage: int
    :param current: int
    :param theoretical_max_power: int
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    '''

    generated_power = voltage * current
    efficiency = (float(generated_power) / theoretical_max_power) * 100
    print(efficiency)
    if efficiency >= 80 and efficiency <= 100:
        return 'green'
    elif efficiency >= 60 and efficiency <= 79:
        return 'orange'
    elif efficiency >= 30 and efficiency <= 59:
        return 'red'
    elif efficiency >=0 and efficiency < 30:
        return 'black'
    else:
        return 'Out of range'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    '''

    :param temperature:
    :param neutrons_produced_per_second:
    :param threshold:
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    '''

    criticality = (float(temperature * neutrons_produced_per_second)/threshold) * 100
    print(criticality)
    if criticality < 40 and criticality > 0:
        return 'LOW'
    elif criticality >= 90.0 and criticality <= 110.1:
        return 'NORMAL'
    else:
        return 'DANGER'

if __name__ == '__main__':
    #print(is_criticality_balanced(750, 900))
    print(fail_safe(temperature=100, neutrons_produced_per_second=55, threshold=5000))
