import csv
import time
import requests
from bs4 import BeautifulSoup
import os 

def get_cpt_code_summary(cpt_code):
    # URL to fetch
    url = f"https://www.aapc.com/codes/cpt-codes/{cpt_code}"

    # Fetch the content of the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant section that contains the summary
        summary_tag = soup.find('div', class_='panel-body').find('p')

        if summary_tag:
            summary = summary_tag.get_text(strip=True)
            return summary
        else:
            return "Summary not found."
    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}"

# List of CPT codes
cpt_codes = [
    "77067", "77063", "71046", "71045", "77080",
    "72148", "73721", "76700", "74177", "73030",
    "76641", "72100", "73630", "70450", "76830",
    "74018", "76536", "76856", "73502", "73562"
]

cpt_codes = ['97116',
 '90648',
 '93041',
 '99392',
 '11305',
 '15788',
 '97162',
 '97802',
 '99498',
 '91320',
 '90647',
 '94060',
 '97035',
 '74022',
 '17110',
 '90674',
 '98960',
 '92583',
 '96361',
 '99385',
 '20551',
 '90792',
 '76802',
 '99456',
 '99058',
 '99377',
 '86618',
 '72110',
 '57160',
 '11750',
 '94010',
 '99415',
 '99425',
 '87075',
 '99395',
 '93271',
 '90620',
 '97112',
 '97551',
 '90736',
 '99453',
 '87591',
 '99499',
 '99396',
 '11401',
 '99211',
 '10140',
 '11720',
 '99355',
 '16025',
 '90685',
 '95251',
 '99421',
 '76805',
 '76816',
 '90473',
 '99483',
 '90632',
 '76856',
 '90696',
 '91308',
 '98968',
 '99326',
 '99403',
 '96125',
 '99446',
 '99202',
 '99335',
 '96374',
 '99051',
 '90681',
 '96360',
 '90743',
 '86689',
 '64646',
 '99417',
 '98967',
 '11982',
 '90646',
 '90715',
 '11300',
 '97598',
 '97163',
 '97164',
 '90682',
 '86328',
 '93247',
 '91321',
 '99383',
 '86592',
 '90636',
 '11111',
 '99402',
 '76700',
 '90700',
 '82950',
 '88164',
 '64612',
 '57454',
 '90714',
 '20600',
 '90672',
 '93010',
 '81003',
 '90686',
 '95992',
 '81001',
 '90461',
 '90650',
 '83036',
 '90680',
 '90702',
 '90688',
 '84703',
 '64615',
 '82947',
 '99284',
 '90739',
 '99998',
 '71046',
 '90716',
 '93793',
 '99072',
 '99458',
 '10121',
 '94664',
 '88150',
 '57452',
 '71101',
 '93243',
 '93975',
 '99243',
 '87804',
 '90472',
 '80305',
 '90651',
 '96375',
 '90678',
 '93922',
 '87651',
 '96103',
 '90670',
 '93227',
 '99001',
 '87880',
 '90723',
 '85610',
 '97535',
 '99394',
 '88155',
 '36416',
 '11306',
 '99173',
 '76817',
 '88106',
 '11981',
 '73100',
 '74018',
 '90675',
 '23071',
 '87110',
 '99375',
 '80048',
 '84704',
 '87084',
 '87491',
 '82274',
 '99000',
 '82272',
 '99994',
 '20610',
 '88160',
 '94761',
 '11200',
 '90734',
 '99455',
 '97760',
 '36410',
 '73140',
 '87426',
 '93268',
 '99409',
 '57505',
 '99447',
 '96365',
 '93000',
 '87430',
 '99214',
 '91313',
 '99496',
 '72050',
 '96373',
 '99382',
 '17111',
 '97161',
 '90655',
 '93242',
 '99995',
 '12002',
 '91307',
 '99215',
 '11000',
 '90750',
 '99381',
 '87502',
 '20200',
 '90619',
 '90710',
 '98969',
 '76857',
 '82948',
 '99439',
 '90732',
 '87635',
 '99452',
 '99474',
 '11103',
 '73110',
 '81025',
 '87811',
 '93042',
 '99080',
 '90657',
 '57421',
 '88175',
 '81528',
 '99344',
 '93784',
 '95943',
 '15853',
 '99345',
 '51702',
 '15850',
 '90698',
 '99177',
 '31000',
 '93270',
 '99203',
 '73501',
 '69209',
 '69200',
 '51701',
 '97530',
 '80304',
 '99002',
 '11102',
 '85018',
 '80100',
 '82962',
 '29130',
 '29580',
 '99457',
 '99487',
 '82270',
 '11301',
 '90460',
 '80061',
 '99490',
 '99407',
 '99050',
 '99349',
 '96372',
 '99354',
 '86631',
 '99205',
 '73521',
 '91305',
 '91312',
 '15852',
 '76705',
 '76536',
 '76815',
 '96127',
 '96132',
 '99347',
 '90713',
 '99387',
 '11056',
 '82607',
 '76706',
 '99411',
 '93224',
 '91300',
 '99391',
 '97803',
 '85025',
 '91306',
 '15851',
 '90740',
 '99495',
 '11310',
 '93248',
 '72040',
 '76810',
 '99341',
 '57420',
 '99406',
 '20605',
 '95012',
 '11721',
 '81000',
 '96136',
 '99358',
 '92587',
 '99441',
 '78267',
 '99334',
 '56605',
 '95923',
 '10120',
 '11404',
 '72100',
 '17340',
 '73070',
 '90744',
 '99423',
 '72120',
 '87802',
 '99999',
 '90887',
 '90679',
 '99443',
 '11104',
 '73080',
 '96160',
 '90474',
 '73560',
 '92283',
 '99188',
 '90733',
 '99350',
 '90703',
 '86480',
 '87420',
 '11730',
 '90621',
 '90630',
 '86580',
 '90746',
 '91303',
 '76813',
 '99454',
 '72170',
 '90697',
 '97597',
 '99386',
 '99343',
 '90480',
 '93976',
 '82271',
 '99242',
 '11302',
 '17003',
 '99336',
 '90677',
 '87807',
 '99342',
 '76830',
 '90656',
 '92551',
 '90694',
 '81005',
 '86769',
 '99337',
 '12001',
 '10060',
 '99374',
 '95115',
 '90634',
 '87177',
 '97550',
 '99244',
 '87400',
 '94150',
 '11400',
 '71100',
 '11403',
 '59025',
 '93040',
 '65205',
 '99199',
 '86308',
 '81099',
 '90687',
 '17250',
 '95117',
 '83655',
 '73120',
 '99212',
 '95249',
 '99359',
 '11042',
 '78268',
 '99408',
 '94640',
 '99424',
 '73562',
 '19453',
 '57455',
 '51798',
 '99489',
 '80307',
 '97032',
 '17000',
 '76801',
 '99310',
 '81002',
 '99325',
 '99348',
 '93005',
 '87210',
 '93244',
 '92552',
 '90649',
 '91315',
 '92014',
 '80300',
 '58322',
 '80306',
 '99401',
 '84702',
 '99416',
 '25111',
 '90660',
 '69210',
 '90471',
 '10061',
 '94760',
 '99327',
 '90662',
 '94618',
 '91322',
 '99384',
 '58100',
 '97140',
 '99024',
 '99442',
 '16020',
 '57410',
 '95250',
 '73620',
 '99241',
 '99404',
 '83014',
 '93246',
 '99429',
 '57415',
 '87512',
 '96110',
 '11055',
 '97110',
 '99174',
 '90644',
 '73610',
 '74019',
 '99397',
 '73630',
 '76819',
 '87081',
 '11307',
 '99204',
 '73502',
 '90633',
 '51700',
 '98966',
 '80101',
 '87428',
 '90756',
 '99437',
 '64405',
 '73130',
 '99213',
 '90658',
 '99379',
 '99393',
 '99459',
 '88142',
 '99473',
 '87270',
 '84443',
 '56420',
 '73030',
 '15854',
 '99497',
 '99201',
 '91309',
 '77066',
 '20550',
 '72070',
 '93325',
 '58301',
 '36415',
 '96161',
 '99605',
 '99702',
 '90671',
 '20553',
 '10000',
 '85013',
 '87592',
 '99491',
 '90833',
 '97602',
 '20552',
 '90669',
 '87636',
 '90707']


# Function to get the existing CPT codes from the file
def get_existing_cpt_codes(file_path):
    if not os.path.exists(file_path):
        return set()  # Return an empty set if the file doesn't exist yet

    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        existing_cpts = {row[0] for row in reader}
    return existing_cpts

# File path
file_path = 'cpt_code_descriptions_aapc.csv'

# Get existing CPT codes from the file
existing_cpts = get_existing_cpt_codes(file_path)

# Open the file in append mode to write new descriptions
with open(file_path, mode='a', newline='') as file:
    writer = csv.writer(file)

    # Loop through the list of CPT codes and write their summaries to the file
    for cpt_code in cpt_codes:
        if cpt_code in existing_cpts:
            print(f"CPT Code {cpt_code} already exists. Skipping...")
            continue

        summary = get_cpt_code_summary(cpt_code)
        print(summary)
        time.sleep(1)
        writer.writerow([cpt_code, summary])
