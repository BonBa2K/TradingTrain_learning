def pord_serializer(pord) -> dict:

    return {
        "_id": str(pord["_id"]),
        "prod_name": pord["prod_name"],
        "prod_price": pord["prod_price"],
        "channel": pord["channel"],
        "created_at": pord["created_at"]
    }
    


def pords_serializer(pords) -> list:
    Output = []
    for pord in pords:
        Output.append(pord_serializer(pord))
    return Output
