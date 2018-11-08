from __future__ import unicode_literals

import json

from moto.core.responses import BaseResponse

from .models import dynamodbstreams_backends


class DynamoDBStreamsHandler(BaseResponse):

    @property
    def backend(self):
        return dynamodbstreams_backends[self.region]
    
    def describe_stream(self):
        arn = self._get_param('StreamArn')
        return self.backend.describe_stream(arn)

    def list_streams(self):
        table_name = self._get_param('TableName')
        return self.backend.list_streams(table_name)

    def get_shard_iterator(self):
        arn = self._get_param('StreamArn')
        shard_id = self._get_param('ShardId')
        shard_iterator_type = self._get_param('ShardIteratorType')
        return self.backend.get_shard_iterator(arn, shard_id,
                                               shard_iterator_type)

    def get_records(self):
        arn = self._get_param('ShardIterator')
        limit = self._get_param('Limit')
        if limit is None:
            limit = 1000
        return self.backend.get_records(arn, limit)
