"""Auto-generated file, do not edit by hand. CD metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CD = PhoneMetadata(id='CD', country_code=243, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[89]\\d{8}|[1-6]\\d{6}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-6]\\d{6}', possible_number_pattern='\\d{7}', example_number='1234567'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:8[0-2489]|9[7-9])\\d{7}', possible_number_pattern='\\d{9}', example_number='991234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([89]\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([1-6]\\d)(\\d{5})', format=u'\\1 \\2', leading_digits_pattern=['[1-6]'], national_prefix_formatting_rule=u'0\\1')])
