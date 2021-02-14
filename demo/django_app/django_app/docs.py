OPENAPI_VERSION = 'openapi: 3.0.2'
OPENAPI_INFO = '''
title: Swagger Petstore - OpenAPI 3.0
description: >-
  This is a sample Pet Store Server based on the OpenAPI 3.0 specification. 
  You can find out more about

  Swagger at [http://swagger.io](http://swagger.io). In the third iteration of
  the pet store, we've switched to the design first approach!

  You can now help us improve the API whether it's by making changes to the
  definition itself or to the code.

  That way, with time, we can improve the API in general, and expose some of
  the new features in OAS3.


  Some useful links:

  - [The Pet Store
  repository](https://github.com/swagger-api/swagger-petstore)

  - [The source API definition for the Pet
  Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)
termsOfService: 'http://swagger.io/terms/'
contact:
  email: apiteam@swagger.io
license:
  name: Apache 2.0
  url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
version: 1.0.5
'''

OPENAPI_EXTERNALDOCS = '''
description: Find out more about Swagger
url: 'http://swagger.io'
'''

OPENAPI_SERVERS = '''
- url: /api/v3
'''

OPENAPI_TAGS = '''
- name: pet
  description: Everything about your Pets
  externalDocs:
    description: Find out more
    url: 'http://swagger.io'
- name: store
  description: Operations about user
- name: user
  description: Access to Petstore orders
  externalDocs:
    description: Find out more about our store
    url: 'http://swagger.io'
'''

OPENAPI_SCHEMAS = '''
Order:
  type: object
  properties:
    id:
      type: integer
      format: int64
      example: 10
    petId:
      type: integer
      format: int64
      example: 198772
    quantity:
      type: integer
      format: int32
      example: 7
    shipDate:
      type: string
      format: date-time
    status:
      type: string
      description: Order Status
      example: approved
      enum:
        - placed
        - approved
        - delivered
    complete:
      type: boolean
  xml:
    name: order
Customer:
  type: object
  properties:
    id:
      type: integer
      format: int64
      example: 100000
    username:
      type: string
      example: fehguy
    address:
      type: array
      xml:
        name: addresses
        wrapped: true
      items:
        $ref: '#/components/schemas/Address'
  xml:
    name: customer
Address:
  type: object
  properties:
    street:
      type: string
      example: 437 Lytton
    city:
      type: string
      example: Palo Alto
    state:
      type: string
      example: CA
    zip:
      type: string
      example: '94301'
  xml:
    name: address
Category:
  type: object
  properties:
    id:
      type: integer
      format: int64
      example: 1
    name:
      type: string
      example: Dogs
  xml:
    name: category
User:
  type: object
  properties:
    id:
      type: integer
      format: int64
      example: 10
    username:
      type: string
      example: theUser
    firstName:
      type: string
      example: John
    lastName:
      type: string
      example: James
    email:
      type: string
      example: john@email.com
    password:
      type: string
      example: '12345'
    phone:
      type: string
      example: '12345'
    userStatus:
      type: integer
      description: User Status
      format: int32
      example: 1
  xml:
    name: user
Tag:
  type: object
  properties:
    id:
      type: integer
      format: int64
    name:
      type: string
  xml:
    name: tag
Pet:
  required:
    - name
    - photoUrls
  type: object
  properties:
    id:
      type: integer
      format: int64
      example: 10
    name:
      type: string
      example: doggie
    category:
      $ref: '#/components/schemas/Category'
    photoUrls:
      type: array
      xml:
        wrapped: true
      items:
        type: string
        xml:
          name: photoUrl
    tags:
      type: array
      xml:
        wrapped: true
      items:
        $ref: '#/components/schemas/Tag'
    status:
      type: string
      description: pet status in the store
      enum:
        - available
        - pending
        - sold
  xml:
    name: pet
ApiResponse:
  type: object
  properties:
    code:
      type: integer
      format: int32
    type:
      type: string
    message:
      type: string
  xml:
    name: '##default'
'''

OPENAPI_COMPONENTS = '''
requestBodies:
  Pet:
    description: Pet object that needs to be added to the store
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Pet'
      application/xml:
        schema:
          $ref: '#/components/schemas/Pet'
  UserArray:
    description: List of user object
    content:
      application/json:
        schema:
          type: array
          items:
            $ref: '#/components/schemas/User'
securitySchemes:
  petstore_auth:
    type: oauth2
    flows:
      implicit:
        authorizationUrl: 'https://petstore3.swagger.io/oauth/authorize'
        scopes:
          'write:pets': modify pets in your account
          'read:pets': read your pets
  api_key:
    type: apiKey
    name: api_key
    in: header
schemas:
''' + '\n  '.join([''] + OPENAPI_SCHEMAS.split('\n'))
