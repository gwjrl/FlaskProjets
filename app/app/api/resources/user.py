from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
# from app.api.schemas import UserSchema
from app.models import User
from extensions import db
from app.commons.pagination import paginate


class UserResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  user: UserSchema
        404:
          description: user does not exists
    put:
      tags:
        - api
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              UserSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user updated
                  user: UserSchema
        404:
          description: user does not exists
    delete:
      tags:
        - api
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user deleted
        404:
          description: user does not exists
    """

    method_decorators = [jwt_required()]

    def get(self, user_id):
        # schema = UserSchema()
        # user = User.query.get_or_404(user_id)
        # return {"user": schema.dump(user)}
        pass

    def put(self, user_id):
        # schema = UserSchema(partial=True)
        # user = User.query.get_or_404(user_id)
        # user = schema.load(request.json, instance=user)
        #
        # db.session.commit()
        #
        # return {"msg": "user updated", "user": schema.dump(user)}
        pass

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}


class UserList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/UserSchema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              UserSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user created
                  user: UserSchema
    """

    method_decorators = [jwt_required()]

    def get(self):
        # schema = UserSchema(many=True)
        # query = User.query
        # return paginate(query, schema)
        pass

    def post(self):
        # schema = UserSchema()
        # user = schema.load(request.json)
        #
        # db.session.add(user)
        # db.session.commit()
        #
        # return {"msg": "user created", "user": schema.dump(user)}, 201
        pass
