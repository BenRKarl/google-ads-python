# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import customer_label_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_customer__label__pb2
from google.ads.google_ads.v1.proto.services import customer_label_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_customer__label__service__pb2


class CustomerLabelServiceStub(object):
  """Proto file describing the Customer Label service.

  Service to manage labels on customers.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCustomerLabel = channel.unary_unary(
        '/google.ads.googleads.v1.services.CustomerLabelService/GetCustomerLabel',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_customer__label__service__pb2.GetCustomerLabelRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_customer__label__pb2.CustomerLabel.FromString,
        )
    self.MutateCustomerLabels = channel.unary_unary(
        '/google.ads.googleads.v1.services.CustomerLabelService/MutateCustomerLabels',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_customer__label__service__pb2.MutateCustomerLabelsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_customer__label__service__pb2.MutateCustomerLabelsResponse.FromString,
        )


class CustomerLabelServiceServicer(object):
  """Proto file describing the Customer Label service.

  Service to manage labels on customers.
  """

  def GetCustomerLabel(self, request, context):
    """Returns the requested customer-label relationship in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCustomerLabels(self, request, context):
    """Creates and removes customer-label relationships.
    Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerLabelServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCustomerLabel': grpc.unary_unary_rpc_method_handler(
          servicer.GetCustomerLabel,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_customer__label__service__pb2.GetCustomerLabelRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_customer__label__pb2.CustomerLabel.SerializeToString,
      ),
      'MutateCustomerLabels': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCustomerLabels,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_customer__label__service__pb2.MutateCustomerLabelsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_customer__label__service__pb2.MutateCustomerLabelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.CustomerLabelService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
