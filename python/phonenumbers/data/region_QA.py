"""Auto-generated file, do not edit by hand. QA metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_QA = PhoneMetadata(id='QA', country_code=974, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[3-8]\\d{6,7}', possible_number_pattern='\\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='44\\d{6}', possible_number_pattern='\\d{7,8}', example_number='44123456'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:3[03]|55|66|7[07])\\d{6}', possible_number_pattern='\\d{7,8}', example_number='33123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{4}', possible_number_pattern='\\d{7,8}', example_number='8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(8\\d{2})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['8']),
        NumberFormat(pattern='([3-7]\\d{3})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[3-7]'])])
