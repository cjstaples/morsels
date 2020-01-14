# removed from cashbot, can rebuild cleanly?

import csv
import os
import random
import shutil
import sys
from datetime import datetime, timedelta, date
from optparse import OptionParser

import gnupg
import paramiko
from munch import Munch

"""
Business rules *removed*
"""


# ---------------------------------------------------------------------
def merch_header_list():
    trxmerch_file_headers = [[
        'SeqNum',
        'Amount',
        'Currency',
        'First Name',
        'Last Name',
        'Recipient Email',
        'Recipient Phone Number',
        'Reason',
        'eGift Card Message',
        'Issue Date',
        'Case ID',
        'Notes'
    ]]
    return trxmerch_file_headers


# ---------------------------------------------------------------------
def olmos_header_list():
    trxmerch_olmos_reg_file_headers = [[
        'REGISTRY_NUMBER',
        'RECID',
        'GIFTCARD_EXPDATE',
        'PAYOUT_AMOUNT',
        'GIFT_CARD_ACCOUNT_NUM',    # these fields should be blank on generation
        'PIN',                      # then cashstar populates for return file
        'ACTUAL_GIFTCARD_EXP'
    ]]
    return trxmerch_olmos_reg_file_headers


# ---------------------------------------------------------------------
def last_line_fill(headers):
    """

    :param headers:
    :return:
    """
    return [['##' for _ in headers]]


# ---------------------------------------------------------------------
def gen_sequence_num(count):
    """

    :param count:
    :return:
    """
    return (
        '{count}'.format(count=count).zfill(40) if count == 1
        else ['{i}'.format(i=i).zfill(40) for i in range(1, count)]
    )


# ---------------------------------------------------------------------
def gen_olmos_registry_num(count):
    """

    :param count:
    :return:
    """
    registry_num_list = []

    while count:
        val = create_n_sized_int_value(15)
        if val not in registry_num_list:
            registry_num_list.append(val)
            count -= 1

    return registry_num_list


# ---------------------------------------------------------------------
def gen_amount(opts):
    """
    if an amount was passed in then use it otherwise generate a random amount

    :param opts:
    """
    return_amount = 0.0
    if opts['amount']:
        return_amount = opts['amount']
    else:
        # if opts['merchandise_return']:
        amt_list = [
            # '1.00', '5.00',
            '10.00', '25.00', '50.00',
            '75.00', '100.00', '250.00', '500.00'  # ,
            # '1000.00', '10000.00', '100000.00'
            #  spec allows a larger amount
            # but our constraints in semi --> min == $10 max == $500,
            # so keep it as max for now
        ]
        return_amount = amt_list[random.randint(0, len(amt_list) - 1)]

        # if opts['endless_rewards']:
        #     return_amount = float(create_n_sized_int_value(7))

    return '{:7.2f}'.format(float(return_amount))


# ---------------------------------------------------------------------
def gen_currency_code(opts):
    """

    :param opts:
    :return:
    """
    currency_dict = {
        'US': 'USD',
        'CA': 'CAD'
    }
    return currency_dict[opts['country']]


# ---------------------------------------------------------------------
def random_substring_generator(in_string):
    """

    :param in_string:
    :return:
    """
    return_string = in_string[:random.randint(0, len(in_string))]
    return return_string if return_string != '' else in_string


# ---------------------------------------------------------------------
def gen_name(name_string, variable_size):
    """
   :param name_string:
   :param variable_size:
   :return:
   """
    return (
        random_substring_generator(name_string)
        if variable_size else name_string
    )


# ---------------------------------------------------------------------
def gen_firstname(opts):
    """
    :param opts:
    :return:
    """
    return gen_name("maxfirstname", opts['variable_fields'])


# ---------------------------------------------------------------------
def gen_lastname(opts):
    """
    :param opts:
    :return:
    """
    return gen_name("amaxlastname", opts['variable_fields'])


# ---------------------------------------------------------------------
def gen_recid():
    """
    :return:
    """
    return create_n_sized_int_value(20)


# ---------------------------------------------------------------------
def gen_recipient_email(opts):
    """
    :param opts:
    :return:
    """
    # max_length = 50   # in case we want to test this, hold off for now
    return opts['email'] if opts['email'] != '' else 'cashstartest@gmail.com'


# ---------------------------------------------------------------------
def get_optional_field_value(opts):
    retval = random.randint(0, 10)
    if opts['optional_fields'] != 'rand':
        if opts['optional_fields'] == 'all':
            retval = 0
        if opts['optional_fields'] == 'none':
            retval = 9
    return retval


# ---------------------------------------------------------------------
def gen_recipient_phone_num(opts):
    """
   :param opts:
   :return:
   """
    populate_phone_num = get_optional_field_value(opts)

    if populate_phone_num > 7:
        return ''
    else:
        # http://stackoverflow.com/questions/26226801/making-random-phone-number-xxx-xxx-xxxx
        # better than my half-ass'd approach
        n = '0000000000'
        while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
            n = to_unicode(random.randint(10**9, 10**10-1))
        return n[:3] + '-' + n[3:6] + '-' + n[6:]


# ---------------------------------------------------------------------
def gen_egc_message(opts):

    retstr = (
        "This is a text representation of a number of characters including "
        "the whitespace. The purpose of this "
        "text is to test the character limit of the text area where the gift "
        "giver can send a message to the gift "
        "recipient. The maximum limit should be this. ok"
    )

    has_egc_message = get_optional_field_value(opts)

    return (
        random_substring_generator(retstr)
        if opts['variable_fields'] else retstr
    ) if has_egc_message < 7 else ''


# ---------------------------------------------------------------------
def gen_issue_date():
    return datetime.now() + timedelta(-random.randint(0, 31))


# ---------------------------------------------------------------------
def create_n_sized_int_value(n):
    """

    :param n:
    :return: string of numbers n long
    """
    return random_substring_generator(
        to_unicode(random.randint(0, (10**n)-1))
    ).zfill(n)


# ---------------------------------------------------------------------
def gen_return_reason_code(opts):

    has_return_reason = get_optional_field_value(opts)

    return_string = create_n_sized_int_value(20)
    return (
        random_substring_generator(return_string)
        if opts['variable_fields'] else return_string
    ) if has_return_reason < 7 else ''


# ---------------------------------------------------------------------
def gen_case_id(opts):

    has_case_id = get_optional_field_value(opts)

    return_string = create_n_sized_int_value(40)
    return (
        random_substring_generator(return_string)
        if opts['variable_fields'] else return_string
    ) if has_case_id < 7 else ''


# ---------------------------------------------------------------------
def gen_notes(opts):

    has_notes = get_optional_field_value(opts)
    return_string = "If we had anything else to add it'd be here extraa"
    return (random_substring_generator(return_string)
            if opts['variable_fields'] else return_string
            ) if has_notes < 7 else ''


# ---------------------------------------------------------------------
def gc_exp_date():

    does_not_expire = random.randint(0, 100)
    return (
        date(2149, 12, 31) if does_not_expire > 50 # 84
        else datetime.now() + timedelta((30 * 6) + random.randint(0, 45))
    )


# ---------------------------------------------------------------------
def generate_data_row(n, opts):
    """
    :param n:
    :param opts:
    """

    if opts['bad_data']:
        # any of these should fail for their respective fields
        bd = opts['bad_data']
        sequence = to_unicode(n) if bd not in [
            'seq_num', 'all_merch'
        ] else 'ZYXWVUTSRQPONMLKJIHGFEDCBA,'

        amount = to_unicode(gen_amount(opts)) if bd not in [
            'amount', 'all_merch'
        ] else '-X13,'

        currency = gen_currency_code(opts) if bd not in [
            'currency', 'all_merch'
        ] else '@@@,'

        first_name = gen_firstname(opts) if bd not in [
            'first', 'all_merch'
        ] else 'M as 1n Manc33,'

        last_name = gen_lastname(opts) if bd not in [
            'last', 'all_merch'
        ] else '1337 1^57N^_^^3,'

        email = gen_recipient_email(opts) if bd not in [
            'email', 'all_merch'
        ] else 'notanemail,eh?'

        phone = gen_recipient_phone_num(opts) if bd not in [
            'phone', 'all_merch'
        ] else '0000G0000,'

        reason = (gen_return_reason_code(opts) if bd not in [
            'reason', 'all_merch'
        ] else '987654321001234567899'  # exceed max length 20
                  )

        message = (gen_egc_message(opts) if bd not in [
            'message', 'all_merch'
        ] else -1  # how to fail - not sure this won't pass
                   )

        dtm = gen_issue_date().strftime('%d/%m/%Y %H:%M:%S') if bd not in [
            'issue_date', 'all_merch'
        ] else '$7.77'

        case_id = (gen_case_id(opts) if bd not in [
            'case_id', 'all_merch'
        ] else '987654321001234567899987654321001234567899876543210'
                   )  # exceed max length 50

        notes = (gen_notes(opts) if bd not in [
            'notes', 'all_merch'
        ] else '987654321001234567899987654321001234567899876543210'
                 )  # exceed max length 50
    else:
        sequence = to_unicode(n)
        amount = to_unicode(gen_amount(opts))
        currency = gen_currency_code(opts)
        first_name = gen_firstname(opts)
        last_name = gen_lastname(opts)
        email = gen_recipient_email(opts)
        phone = gen_recipient_phone_num(opts)
        reason = gen_return_reason_code(opts)
        message = gen_egc_message(opts)
        dtm = gen_issue_date().strftime('%d/%m/%Y %H:%M:%S')
        case_id = gen_case_id(opts)
        notes = gen_notes(opts)

    return_list = [
        sequence, amount, currency,
        first_name, last_name, email,
        phone, reason, message,
        dtm, case_id, notes
    ]

    return [return_list]


# ---------------------------------------------------------------------
def create_csv_rows(opts, case=None):
    """

    :param opts:
    :param case:
    :return:
    """
    if opts['regression']:
        if case == 'empty':
            return ['\n']
        else:
            return generate_data_row(gen_sequence_num(1), opts)
    else:
        return [
            generate_data_row(n, opts) for n
            in gen_sequence_num(opts['trx_merch_lines'])
            ]


# ---------------------------------------------------------------------
def create_txt_pipe_rows(opts):
    """

    ::
    :param opts:
    :return:
    """
    retstr = [
        [n, gen_recid(), gc_exp_date().strftime('%m/%d/%Y'),
         gen_amount(opts), '', '', '']
        for n in gen_olmos_registry_num(opts['trx_endlessrewards_lines'])
        ]
    retstr[:0] = [olmos_header_list()[0]]   # add headers, not in test file or spec...so not sure these are required
    return retstr


# ---------------------------------------------------------------------
def write_csv_file_for_trxmerch(in_file_name, row_list):
    """

        <batch value>_<date>.csv
    :param in_file_name:
    :param row_list:
    :return:
    """
    with open(in_file_name, 'wb') as csvfile:
        fw = csv.writer(csvfile, delimiter=to_unicode(','))
        fw.writerows(merch_header_list())
        for order_row in row_list:
            fw.writerows(order_row)
        fw.writerows(last_line_fill(merch_header_list()[0]))


# ---------------------------------------------------------------------
def write_pipe_file_for_olmos_trx_registry(in_file_name,
                                           row_list,
                                           recip_gpg_key_id,
                                           gpg_key_password,
                                           opts):
    """
    :param in_file_name:
    :param row_list:
    :param recip_gpg_key_id:
    :param gpg_key_password:
    """
    # thanks again Joe

    # wrong send key in semi??? need to fix, this has been domne once - find edits
    # set this up to do local testing, but its broken and i can't find the original
    #  fix that i thought had been checked in.

    if opts['local_testing'] and 'semi' in opts['server']:
        gpg_send_key = '97EF5093' if recip_gpg_key_id == 'E1CCFC2E' else recip_gpg_key_id
    else:
        gpg_send_key = recip_gpg_key_id     # may still be wrong for semi, should work in qa

    settings = Munch(
        GPG_HOME=(os.environ['HOME'] + '/.gnupg/'),
        GPG_BINARY='/usr/local/bin/gpg',
        GPG_PUBLIC_KEYRING='pubring.gpg',
        GPG_PRIVATE_KEYRING='secring.gpg',
        GPG_RECIPIENT_KEY_ID=recip_gpg_key_id,  # public key ID for the recipient,
        # not the same key we use for decrypting
        GPG_SENDER_KEY_ID=gpg_send_key,
        GPG_SENDER_KEY_PASSPHRASE=gpg_key_password,
    )

    # file body
    data_string = '|'.join(row_list[0]) + '\n'
    for order_row in row_list[1:]:
        data_string += "|".join(order_row) + '\n'
    # keeping this in place for now for testing,
    # remove after validation that files are working
    with open('endless_earnings_test_file.txt', 'w') as f:
        f.write(data_string)

    encrypted_filename = in_file_name  # this will be moved out onto ftp

    _gpg = gnupg.GPG(binary=settings.GPG_BINARY,
                     homedir=settings.GPG_HOME,
                     keyring=settings.GPG_PUBLIC_KEYRING,
                     secring=settings.GPG_PRIVATE_KEYRING)

    _gpg.encrypt(data_string,
                 settings.GPG_RECIPIENT_KEY_ID,
                 default_key=settings.GPG_SENDER_KEY_ID,  # Used for signing
                 passphrase=settings.GPG_SENDER_KEY_PASSPHRASE,
                 armor=True,  # False,
                 encrypt=True,
                 symmetric=False,  # Don't combine symmetric and signing or else you
                 # will leak the pass phrase!
                 always_trust=True,  # Ignore trust warnings on recipient key
                 output=encrypted_filename)


# --------------------------------------------------------------------
def generate_merch_filename(opts):
    """

    :param opts:
    :return:
    """
    return '{root}/{name}_{dtm}{ext}'.format(
        root=opts['local_directory'],
        name=to_unicode(random.randint(0, 99999)).zfill(5),
        dtm=datetime.today().strftime('%m%d%Y'),
        ext='.csv'
    )


# ---------------------------------------------------------------------
def generate_olmos_registry_filename(opts):
    """
    :param opts:
    :return:
    """
    return '{root}/OLMOS_CS_DEFUNCT_LOSINGS_REC_{dtm}{ext}'.format(
        root=opts['local_directory'],
        dtm=datetime.today().strftime('%Y%m%d'),
        ext='.gpg'
    )


# ---------------------------------------------------------------------
def generate_files(opts, name=None):
    """
    :param opts:
    :param name:
    """
    # todo - better way to do the naming & filtering? this feels gross
    if opts['merchandise_return']:

        file_name = '{root}{sep}{name}_{dtm}{ext}'.format(
            root=opts['local_directory'],
            sep=os.path.sep,
            name=name,
            dtm=datetime.today().strftime('%m%d%Y'),
            ext='.csv'
        )

        with open(file_name, 'wb') as f:

            fw = csv.writer(f, delimiter=to_unicode(','), lineterminator='\n')

            if name == '00008':  # empty line before header
                out_line = []
                fw.writerow(out_line)

            if name not in ['00002', '00004', '00007']:  # no header
                fw.writerows(merch_header_list())
            # no data
            if name not in ['00001', '00002', '00006', '00007']:
                out_line = create_csv_rows(opts)
                fw.writerows(out_line)
            else:
                out_line = []  # create_csv_rows(opts, case='empty')
                fw.writerow(out_line)

            if name not in ['00002', '00003', '00006']:  # no footer
                fw.writerows(last_line_fill(merch_header_list()[0]))

            if name == '00005':  # extra row after footer
                out_line = create_csv_rows(opts)
                fw.writerows(out_line)

    if opts['defunct_losings']:
        # test the empty file case
        file_name = generate_olmos_registry_filename(opts)
        with open(file_name, 'wb') as f:
            fw = csv.writer(f, delimiter=to_unicode('|'), lineterminator='\n')
            out_line = [[]]
            fw.writerow(out_line)


# ---------------------------------------------------------------------
def generate_baseline_files(opts):
    """
    :param opts:
    :return:
    """
    if not os.path.exists(opts['local_directory']):
        print('problem, file directory to send from is missing, unexpected.')
        sys.exit(1)

    if opts['merchandise_return']:
        # hardcoded mainly to keep a record of consistency in naming
        name_dict = ({
            'good_file_name_part': '00000',
            'empty_good_file_name_part': '00001',

            # fail files below - problems if any of these pass
            'empty_file_name_part': '00002',
            'missing_footer_name_part': '00003',
            'data_after_footer_name_part': '00005',
            'missing_header_name_part': '00004',
            'only_header_name_part': '00006',
            'only_footer_name_part': '00007',
            'empty_line_before_header': '00008'  # this one may be legit
            # though it currently fails.
            # need to figure out if blank leading line is valid if rest
            # of file complies.

        })

        if opts['bad_data']:
            name_dict.update({'bad_data': '00009'})

        for k, v in name_dict.items():
            generate_files(opts, v)
            # sys.exit() # for testing remove after regression is completed
    if opts['endless_rewards']:
        generate_files(opts)


# ---------------------------------------------------------------------
def create_and_move_baseline_orders_for_regression(creds, opts):
    """
    :param creds:
    :param opts:
    """
    generate_baseline_files(opts)

    if not os.path.exists(opts['local_directory']):
        os.mkdir(opts['local_directory'])
        print('problem, baseline files missing')
        sys.exit(1)

    move_files_to_ftp_via_paramiko(creds, opts)


# ---------------------------------------------------------------------
def create_and_ftp_deliver_files(opts):
    """
    :param opts:
    """

    if opts['merchandise_return']:
        [
            write_csv_file_for_trxmerch(
                generate_merch_filename(opts),
                create_csv_rows(opts)
            )
            for _ in range(opts['filenum'])
            ]

    if opts['defunct_losings']:
        write_pipe_file_for_olmos_trx_registry(
            generate_olmos_registry_filename(opts),
            create_txt_pipe_rows(opts),
            opts['gpg_key_id'],
            opts['gpg_key_password'],
            opts
        )

    # move the file to the ftp location
    if opts['deliver']:
        move_files_to_ftp_via_paramiko(credentials(opts), opts)


# ---------------------------------------------------------------------
def credentials(opts):
    """
    :param opts:
    """
    return {
        'host': opts['server'],
        'port': 22,
        'username': opts['user'],
        'password': opts['password']
    }


# ---------------------------------------------------------------------
def move_files_to_ftp_via_paramiko(creds, opts):
    #
    paramiko.util.log_to_file('./paramiko.log')
    if not os.path.exists(opts['local_directory']):
        print('problem, file directory to send from is missing, unexpected.')
        sys.exit(1)

    print('Connecting to SFTP.')
    transport = paramiko.Transport((creds['host'], creds['port']))
    transport.connect(username=creds['username'], password=creds['password'])
    sftp = paramiko.SFTPClient.from_transport(transport)
    print('Changing to remote directory.')
    sftp.chdir(opts['remote_path'])
    for f in os.listdir(opts['local_directory']):
        remote = os.path.join(opts['remote_path'], f)
        local = os.path.join(opts['local_directory'], f)
        print(('Uploading {local} to {remote}...'.format(remote=remote, local=local)))
        sftp.put(local, remote)
    sftp.close()
    transport.close()
    print('FTP xfer Complete.')
    if os.path.exists(opts['local_directory']):
        shutil.rmtree(opts['local_directory'])
    if not os.path.exists(opts['local_directory']):
        print('local directory cleaned up and removed.')


# ---------------------------------------------------------------------
def parse_the_options():
    """
    """
    parser = OptionParser()
    parser.add_option("-u", "--user",
                      help="the user you use to deliver to ftp locations.", metavar="FTPUSER")
    parser.add_option("-s", "--server",
                      help="ftp host address, i.e. ftp1.qa.cashstar.net")
    parser.add_option("-p", "--password",
                      help="ftp user password")
    parser.add_option("-m", "--merchandise_return", action="store_true",
                      help="this is the task we want to run")
    parser.add_option("-e", "--endless_rewards", action="store_true",
                      help="this is the task we want to run")
    parser.add_option("-f", "--filenum",
                      help="number of files to generate", type=int, default=1)
    parser.add_option("-M", "--trx_merch_lines",
                      help="number of lines to generate per file. if rand is set, it is a ceiling."
                           "estimated max >= ?????",
                      type=int, default=100)
    parser.add_option("-E", "--trx_defunctrewards_lines",
                      help="number of lines to generate per file. if rand is set, it is a ceiling."
                           "estimated max >= 30000",
                      type=int, default=100)
    parser.add_option("-o", "--optional_fields", choices=["all", "none", "rand"],
                      default="none",
                      help="set population behavior of optional fields")
    parser.add_option("-V", "--variable_fields", action="store_true",
                      default="store_false",
                      help="set if we want variable length data in variable fields")
    parser.add_option("-d", "--deliver", action="store_true", default=False,
                      help="set this to send the file over to the server. "
                           "default is to just print file locally")
    parser.add_option("-C", "--country", choices=["US", "CA"], default="US",
                      help="what country are we in, not sure we care yet or if we will")
    parser.add_option("-q", "--email", default="cashstartest@gmail.com",
                      help="default email, or set your own")
    parser.add_option("-z", "--local_directory", default="./files_out_to_ftp")

    parser.add_option("-L", "--local_testing", default=False,
                      help=("sometimes we want to be able to check what we send."
                            " This will fail processing as the key is set up for"
                            " us to decrypt the file 'sent' to cashstar.")
                      )

    parser.add_option("-r", "--regression", action="store_true",
                      help=("run a regression with baseline files: minimum 1 passing, "
                            "along with a set of failure cases."))
    parser.add_option("-a", "--amount",
                      help="The $ amount to be passed with each line. Exclude to use a random amount.",
                      type=float, default=None)
    parser.add_option("-b", "--bad_data", choices=["phone", "seq_num", "currency", "first", "last", "email",
                                                   "egc_message", "reason", "issue_date", "case_id", "notes",
                                                   "country",
                                                   "all_merch", "reg_num", "recid", "gc_exp_date", "payout",
                                                   "all_reg"
                                                   ],
                      default=None, help="Tune a variable in an otherwise good data set to fail purposefully. "
                                         "A bit of a hodge podge: reg_num, recid, gc_exp_date, payout & all_reg "
                                         "refer to the data regarding the OLMOS Registry file, the rest are TRX MATCH"
                      )

    return parser.parse_args()


# ---------------------------------------------------------------------
def main(argv=None):
    """
    :param argv:
    """
    try:
        if argv is None:
            argv = sys.argv

        # get user options/arguments into dict
        options_list, args = parse_the_options()
        local_options = vars(options_list)

        if not os.path.exists(local_options['local_directory']):
            os.mkdir(local_options['local_directory'])
            assert os.path.exists(local_options['local_directory'])

        # merchandise return set variables here
        if local_options['merchandise_return']:
            local_options.update({'remote_user': 'trxmatch_user'})

        # endless registry set variables
        if local_options['endless_rewards']:
            key_val, pass_val = '', ''
            env = local_options['server'].split('.')[1]
            local_options.update({'remote_user': 'olmos_user'})

            # add encryption keys
            if env == 'qa':
                key_val, pass_val = 'key1', 'val1'
            if env == 'semi':
                key_val, pass_val = 'key2', 'val2'

            local_options.update({
                'gpg_key_id': key_val, 'gpg_key_password': pass_val
            })

        local_options.update({
            'remote_path': '/users/{user}/To-CS'.format(
                user=local_options['remote_user']
            )})

        # everything needing to be pre set should be done, so on to the task
        if local_options['regression']:
            # todo : currently non functional for OLMOS, add regression type test files
            create_and_move_baseline_orders_for_regression(
                credentials(local_options),
                local_options
            )
        else:   # run the job
            create_and_ftp_deliver_files(local_options)

    except Exception:
        raise   # who knows, better safe than sorry
# ---------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
