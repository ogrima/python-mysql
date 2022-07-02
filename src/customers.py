import json

import database_gateway

class Customers:

    def create_record(self, args):

        dg = database_gateway.DatabaseGateway()

        query_string = "insert into customers (first_name, last_name) values (%s, %s)"
        data = (args["first_name"], args["last_name"])

        dg.db_execute(query_string, data)

        return self.read_records(dg.lastrowid)

    def update_record(self, args, resource_id):

        dg = database_gateway.DatabaseGateway()

        query_string = "update customers set first_name = %s, last_name = %s where customer_id = %s"

        data = (args["first_name"], args["last_name"], resource_id)

        dg.db_execute(query_string, data)

        return self.read_records(resource_id)

    def delete_record(self, resource_id):

        dg = database_gateway.DatabaseGateway()

        query_string = "delete from customers where customer_id = %s"

        data = (resource_id,)

        dg.db_execute(query_string, data)

        resp = ("Success",)

        json_object = json.dumps(resp)

        return json.dumps(json.loads(json_object), indent = 2)

    def read_records(self, resource_id):

        dg = database_gateway.DatabaseGateway()

        if resource_id == "" :
            query_string = "select * from customers"
        else:
            query_string = "select * from customers where customer_id = '" + str(resource_id) + "'"

        resp = dg.db_query(query_string)

        return resp