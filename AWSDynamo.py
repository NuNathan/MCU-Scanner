import boto3

dynamodb = boto3.client('dynamodb')

def upload(show, date_GetTime, display_value, premiere):
    dynamodb.put_item(TableName="MCU-Countdown-data", Item={"show":{'S':show}, "date_GetTime":{'N':date_GetTime}, 'display_value':{'S':display_value}, 'premiere':{'S':premiere}})