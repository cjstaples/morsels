import sys
import datetime

def main(argv=None):
    print('(test_misc_data) main:')
    print()

    if argv is None:
        argv = sys.argv

    payment_code = None
    payment_successful = True
    payment_date = datetime.datetime.now()

    data = {
        "transactionId": "123456789012345",
        "currency": "USD",
        "amount": str(99.99),
        "paymentSuccessful": "true" if payment_successful else "false",
        "paymentCode": payment_code if payment_code else "UNAVLB",
        "paymentDate": int(payment_date.timestamp() * 1000),  # this is number of milliseconds since 1/1/1970
    }

    print(data)

    print()
    print('(test_misc_data) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
