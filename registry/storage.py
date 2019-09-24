from absl import logging, flags

import pymongo
from google.protobuf.json_format import MessageToDict, ParseDict
from bson.objectid import ObjectId
from copy import deepcopy

from steward import user_pb2 as u

FLAGS=flags.FLAGS

flags.DEFINE_enum('env', 'dev', ['dev', 'testing', 'prod'], 'Environment to use.')
flags.DEFINE_string('db', 'mongodb://steward.lxc:27017', 'MongoDB connection string.')
flags.DEFINE_integer('db_timeout', 3000, 'MongoDB connection timeout in milliseconds.')

class StorageManager():
    def __init__(self):
        collection = 'steward-' + FLAGS.env
        logging.info('StorageManager connecting to {}/{}'.format(FLAGS.db, collection))
        try:
            self.mongo_client = pymongo.MongoClient(FLAGS.db, serverSelectionTimeoutMS=FLAGS.db_timeout)
            self.db = self.mongo_client[collection]
            self.users = self.db.user
            logging.info(self.mongo_client.server_info())
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(err)

    def encode(self, proto):
        logging.info('Proto->Dict before encode: {}'.format(proto))
        bson = self._proto2dict(proto)
        logging.info('Proto->Dict after encode: {}'.format(bson))
        return bson

    def decode(self, bson, message):
        logging.info('Dict->Proto before decode: {}'.format(bson))
        proto = self._dict2proto(bson, message)
        logging.info('Dict->Proto after decode: {}'.format(proto))
        return proto

    def _proto2dict(self, proto):
        proto_copy = deepcopy(proto)

        if hasattr(proto, '_id') and proto._id: # existing record, encode it and blank the data
            record_id = ObjectId(proto._id)
            proto_copy._id = '' # does not convert cleanly
        dict_out = MessageToDict(message=proto_copy, preserving_proto_field_name=True)

        if hasattr(proto, '_id') and proto._id: # existing record, need to preserve id
            dict_out['_id'] = record_id
        return dict_out

    def _dict2proto(self, bson, message):
        if '_id' in bson:
            bson['_id'] = str(bson['_id']) # ObjectId -> str _id
        proto = message()
        ParseDict(bson, proto)
        return proto
