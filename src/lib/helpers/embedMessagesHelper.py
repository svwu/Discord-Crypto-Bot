import json

def addFieldsFromDataByMap(data,embeddedMessage):
    rawMapFile = open("/app/src/mapping/embedMessages/cmcNameKeyMapping.json", "r")
    mappingInJson = json.loads(rawMapFile.read())['mapping']
    print(data)

    for mappedFieldJson in mappingInJson:
        name = mappedFieldJson['name']

        dataValue = data[mappedFieldJson['key']]
        if(mappedFieldJson['round'] == 'true'):
            dataValue = round(data[mappedFieldJson['key']])
        text = str(dataValue)

        if (mappedFieldJson['slice'] != 0):
            text = text[:mappedFieldJson['slice']]

        value = text + ' ' + mappedFieldJson['additionalText']

        embeddedMessage.add_field(name = name, value = value)

    return embeddedMessage