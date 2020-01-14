from toolz import memoize, partial
import sys


def matches_pairs(pairs, items):
    # return all(pair in item for pair in pairs)
    verbose = False
    results = []
    for pair in pairs:
        pair_key, pair_val = pair
        # print("pair key / val: ", pair_key, pair_val)
        if verbose:
            print("====    ====")
            print("pair: ", pair)

        for item_key, item_val in items.items():
            if verbose:
                print(".. for item...")
                print("pair key / val: ", pair_key, pair_val)
                print("item key / val: ", item_key, item_val)

            if item_key == pair_key:
                if pair_val is None:
                    if item_key == item_key:
                        results.append(True)
                else:
                    if item_val == pair_val:
                        results.append(True)
                    elif isinstance(item_val, list):
                        if f"^{pair_val}" in item_val:
                            results.append(False)
                        elif pair_val in item_val or '*' in item_val:
                            results.append(True)
                        else:
                            results.append(False)
                    else:
                        results.append(False)

    return all(results)

def matching_items(pairs, items):
    return list(filter(partial(matches_pairs, pairs), items))

if __name__ == '__main__':
    print("start: matches")

    criteria_matrix = [
        # (('currency_code', 'USD'), ('credit_card_key', 'visa'), ('security_code','111')),
        # (('currency_code', 'USD'), ('credit_card_key', 'visa'), ('credit_card_type', 'Visa')),
        # (('currency_code', 'USD'), ('credit_card_type', 'Visa')),
        # (('currency_code', 'USD'), ('credit_card_key', 'visa')),
        # (('currency_code', 'USD'), ('credit_card_key', 'mastercard')),
        # (('currency_code', 'USD'), ('credit_card_key', 'americanexpress')),
        # (('currency_code', 'USD'), ('credit_card_key', 'discovercard')),
        # (('currency_code', 'USD'), ('credit_card_key', 'dinersclub')),
        # (('currency_code', 'USD'), ('credit_card_key', 'jcpenney')),
        # (('currency_code', 'USD'), ('credit_card_key', 'nordstrom'))

        (('currency_code', 'USD'), ('credit_card_type', 'Visa')),
        (('currency_code', 'USD'), ('credit_card_type', 'MasterCard')),
        (('currency_code', 'USD'), ('credit_card_type', 'American Express')),
        (('currency_code', 'USD'), ('credit_card_type', 'Discover')),
        (('currency_code', 'USD'), ('credit_card_type', 'Diners Club')),
        (('currency_code', 'USD'), ('credit_card_type', 'JCPenney')),
        (('currency_code', 'USD'), ('credit_card_type', 'Nordstrom')),

        (('currency_code', 'USD'), ('credit_card_type', 'visa')),
        (('currency_code', 'USD'), ('credit_card_type', 'mastercard')),
        (('currency_code', 'USD'), ('credit_card_type', 'americanexpress')),
        (('currency_code', 'USD'), ('credit_card_type', 'discovercard')),
        (('currency_code', 'USD'), ('credit_card_type', 'dinersclub')),
        (('currency_code', 'USD'), ('credit_card_type', 'jcpenney')),
        (('currency_code', 'USD'), ('credit_card_type', 'nordstrom')),
    ]
#    criteria = (('currency_code', 'USD'), ('credit_card_key', 'mastercard'))
#    criteria=(('currency_code', 'USD'), ('credit_card_type', 'MasterCard'))

    credit_card_data=[
        {'credit_card_type': 'Visa', 'credit_card_key': 'visa', 'credit_card_number': '4111111111111111', 'security_code': '111', 'expiration_0': '09', 'expiration_1': '2019', 'currency_code': ['USD']},
        {'credit_card_type': 'Visa', 'credit_card_key': 'visa', 'credit_card_number': '4111111111111111', 'security_code': '737', 'expiration_0': '10', 'expiration_1': '2020', 'currency_code': ['^USD', '*']},
        {'credit_card_type': 'MasterCard', 'credit_card_key': 'mastercard', 'credit_card_number': '5105105105105100', 'security_code': '111', 'expiration_0': '09', 'expiration_1': '2019', 'currency_code': ['USD']},
        {'credit_card_type': 'American Express', 'credit_card_key': 'americanexpress', 'credit_card_number': '340008946251701', 'security_code': '1111', 'expiration_0': '09', 'expiration_1': '2019', 'currency_code': ['USD']},
        {'credit_card_type': 'Discover', 'credit_card_key': 'discovercard', 'credit_card_number': '6011213880179679', 'security_code': '111', 'expiration_0': '09', 'expiration_1': '2019', 'currency_code': ['USD']},
        {'credit_card_type': 'Diners Club', 'credit_card_key': 'dinersclub', 'credit_card_number': '30090797559411', 'security_code': '111', 'expiration_0': '09', 'expiration_1': '2019', 'currency_code': ['USD']},
        {'credit_card_type': 'JCPenney', 'credit_card_key': 'jcpenney', 'credit_card_number': '98990007161', 'currency_code': ['USD']},
        {'credit_card_type': 'Nordstrom', 'credit_card_key': 'nordstrom', 'credit_card_number': '4470415700006342', 'security_code': '114', 'expiration_0': '09', 'expiration_1': '2019', 'currency_code': ['USD']},
        {'credit_card_type': 'Ulta', 'credit_card_key': 'ulta', 'credit_card_number': '5780971055025537', 'currency_code': ['USD']},
        {'credit_card_type': 'BelkPLCC', 'credit_card_key': 'belk', 'credit_card_number': '6045831500905171', 'security_code': '483', 'currency_code': ['USD']},
        {'credit_card_type': 'Belk Mastercard', 'credit_card_key': 'belk-mastercard', 'credit_card_number': '5243001006000180', 'security_code': '663', 'expiration_0': '04', 'expiration_1': '2021', 'currency_code': ['USD']},
        {'credit_card_type': 'Visa', 'credit_card_key': 'visa', 'credit_card_number': '4444333322221111', 'security_code': '737', 'expiration_0': '08', 'expiration_1': '2018', 'currency_code': ['GBP']},
        {'credit_card_type': 'MasterCard', 'credit_card_key': 'mastercard', 'credit_card_number': '5424000000000015', 'security_code': '737', 'expiration_0': '08', 'expiration_1': '2018', 'currency_code': ['GBP']}
    ]

    CARD_TYPES = {
        'Visa': 'VISA',
        'MasterCard': 'MASTERCARD',
        'American Express': 'AMERICANEXPRESS',
        'Discover': 'DISCOVERCARD',
        'Diners Club': 'DINERSCLUB',
        'JCPenney': 'JCP',
        'Nordstrom': 'NORDSTROM',
        'Ulta': 'ULTA',
        'Belk PLCC': 'BELK',
        'Belk Mastercard': 'BELK',  # NOTE: both use same image
    }

    # line 71
    for criteria in criteria_matrix:
        matching_cards = matching_items(criteria, credit_card_data)
    # print("matching_cards:  ", matching_cards)
        print("=====     =====     =====     =====     =====     =====     =====     =====     =====     =====     =====")
        print("criteria: ", criteria)
        # print("     -----     -----     -----     -----     -----     -----     -----     -----     -----     -----")
        if matching_cards:
            for mc in matching_cards:
                print("     mc: ", mc)
        else:
            print("     mc:     NO_MATCH")

    print("exit : matches")
    sys.exit(0)
