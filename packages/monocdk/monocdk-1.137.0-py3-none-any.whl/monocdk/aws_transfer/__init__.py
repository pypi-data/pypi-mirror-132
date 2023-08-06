'''
# AWS Transfer for SFTP Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as transfer
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Transfer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Transfer.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnServer(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_transfer.CfnServer",
):
    '''A CloudFormation ``AWS::Transfer::Server``.

    :cloudformationResource: AWS::Transfer::Server
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_transfer as transfer
        
        cfn_server = transfer.CfnServer(self, "MyCfnServer",
            certificate="certificate",
            domain="domain",
            endpoint_details=transfer.CfnServer.EndpointDetailsProperty(
                address_allocation_ids=["addressAllocationIds"],
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_endpoint_id="vpcEndpointId",
                vpc_id="vpcId"
            ),
            endpoint_type="endpointType",
            identity_provider_details=transfer.CfnServer.IdentityProviderDetailsProperty(
                directory_id="directoryId",
                function="function",
                invocation_role="invocationRole",
                url="url"
            ),
            identity_provider_type="identityProviderType",
            logging_role="loggingRole",
            protocol_details=transfer.CfnServer.ProtocolDetailsProperty(
                passive_ip="passiveIp"
            ),
            protocols=["protocols"],
            security_policy_name="securityPolicyName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            workflow_details=transfer.CfnServer.WorkflowDetailsProperty(
                on_upload=[transfer.CfnServer.WorkflowDetailProperty(
                    execution_role="executionRole",
                    workflow_id="workflowId"
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        certificate: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        endpoint_details: typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", _IResolvable_a771d0ef]] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        identity_provider_details: typing.Optional[typing.Union["CfnServer.IdentityProviderDetailsProperty", _IResolvable_a771d0ef]] = None,
        identity_provider_type: typing.Optional[builtins.str] = None,
        logging_role: typing.Optional[builtins.str] = None,
        protocol_details: typing.Optional[typing.Union["CfnServer.ProtocolDetailsProperty", _IResolvable_a771d0ef]] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        workflow_details: typing.Optional[typing.Union["CfnServer.WorkflowDetailsProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::Transfer::Server``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param certificate: ``AWS::Transfer::Server.Certificate``.
        :param domain: ``AWS::Transfer::Server.Domain``.
        :param endpoint_details: ``AWS::Transfer::Server.EndpointDetails``.
        :param endpoint_type: ``AWS::Transfer::Server.EndpointType``.
        :param identity_provider_details: ``AWS::Transfer::Server.IdentityProviderDetails``.
        :param identity_provider_type: ``AWS::Transfer::Server.IdentityProviderType``.
        :param logging_role: ``AWS::Transfer::Server.LoggingRole``.
        :param protocol_details: ``AWS::Transfer::Server.ProtocolDetails``.
        :param protocols: ``AWS::Transfer::Server.Protocols``.
        :param security_policy_name: ``AWS::Transfer::Server.SecurityPolicyName``.
        :param tags: ``AWS::Transfer::Server.Tags``.
        :param workflow_details: ``AWS::Transfer::Server.WorkflowDetails``.
        '''
        props = CfnServerProps(
            certificate=certificate,
            domain=domain,
            endpoint_details=endpoint_details,
            endpoint_type=endpoint_type,
            identity_provider_details=identity_provider_details,
            identity_provider_type=identity_provider_type,
            logging_role=logging_role,
            protocol_details=protocol_details,
            protocols=protocols,
            security_policy_name=security_policy_name,
            tags=tags,
            workflow_details=workflow_details,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-certificate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "certificate", value)

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-domain
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "domain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointDetails")
    def endpoint_details(
        self,
    ) -> typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.EndpointDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails
        '''
        return typing.cast(typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", _IResolvable_a771d0ef]], jsii.get(self, "endpointDetails"))

    @endpoint_details.setter
    def endpoint_details(
        self,
        value: typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "endpointDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.EndpointType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityProviderDetails")
    def identity_provider_details(
        self,
    ) -> typing.Optional[typing.Union["CfnServer.IdentityProviderDetailsProperty", _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.IdentityProviderDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails
        '''
        return typing.cast(typing.Optional[typing.Union["CfnServer.IdentityProviderDetailsProperty", _IResolvable_a771d0ef]], jsii.get(self, "identityProviderDetails"))

    @identity_provider_details.setter
    def identity_provider_details(
        self,
        value: typing.Optional[typing.Union["CfnServer.IdentityProviderDetailsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "identityProviderDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityProviderType")
    def identity_provider_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.IdentityProviderType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderType"))

    @identity_provider_type.setter
    def identity_provider_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "identityProviderType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingRole")
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.LoggingRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingRole"))

    @logging_role.setter
    def logging_role(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "loggingRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocolDetails")
    def protocol_details(
        self,
    ) -> typing.Optional[typing.Union["CfnServer.ProtocolDetailsProperty", _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.ProtocolDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocoldetails
        '''
        return typing.cast(typing.Optional[typing.Union["CfnServer.ProtocolDetailsProperty", _IResolvable_a771d0ef]], jsii.get(self, "protocolDetails"))

    @protocol_details.setter
    def protocol_details(
        self,
        value: typing.Optional[typing.Union["CfnServer.ProtocolDetailsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "protocolDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::Server.Protocols``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocols
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocols"))

    @protocols.setter
    def protocols(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "protocols", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityPolicyName")
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.SecurityPolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-securitypolicyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyName"))

    @security_policy_name.setter
    def security_policy_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "securityPolicyName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Transfer::Server.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workflowDetails")
    def workflow_details(
        self,
    ) -> typing.Optional[typing.Union["CfnServer.WorkflowDetailsProperty", _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.WorkflowDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-workflowdetails
        '''
        return typing.cast(typing.Optional[typing.Union["CfnServer.WorkflowDetailsProperty", _IResolvable_a771d0ef]], jsii.get(self, "workflowDetails"))

    @workflow_details.setter
    def workflow_details(
        self,
        value: typing.Optional[typing.Union["CfnServer.WorkflowDetailsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "workflowDetails", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnServer.EndpointDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address_allocation_ids": "addressAllocationIds",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_endpoint_id": "vpcEndpointId",
            "vpc_id": "vpcId",
        },
    )
    class EndpointDetailsProperty:
        def __init__(
            self,
            *,
            address_allocation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpc_endpoint_id: typing.Optional[builtins.str] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param address_allocation_ids: ``CfnServer.EndpointDetailsProperty.AddressAllocationIds``.
            :param security_group_ids: ``CfnServer.EndpointDetailsProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnServer.EndpointDetailsProperty.SubnetIds``.
            :param vpc_endpoint_id: ``CfnServer.EndpointDetailsProperty.VpcEndpointId``.
            :param vpc_id: ``CfnServer.EndpointDetailsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                endpoint_details_property = transfer.CfnServer.EndpointDetailsProperty(
                    address_allocation_ids=["addressAllocationIds"],
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if address_allocation_ids is not None:
                self._values["address_allocation_ids"] = address_allocation_ids
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids
            if vpc_endpoint_id is not None:
                self._values["vpc_endpoint_id"] = vpc_endpoint_id
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def address_allocation_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnServer.EndpointDetailsProperty.AddressAllocationIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-addressallocationids
            '''
            result = self._values.get("address_allocation_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnServer.EndpointDetailsProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnServer.EndpointDetailsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.EndpointDetailsProperty.VpcEndpointId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.EndpointDetailsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnServer.IdentityProviderDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_id": "directoryId",
            "function": "function",
            "invocation_role": "invocationRole",
            "url": "url",
        },
    )
    class IdentityProviderDetailsProperty:
        def __init__(
            self,
            *,
            directory_id: typing.Optional[builtins.str] = None,
            function: typing.Optional[builtins.str] = None,
            invocation_role: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param directory_id: ``CfnServer.IdentityProviderDetailsProperty.DirectoryId``.
            :param function: ``CfnServer.IdentityProviderDetailsProperty.Function``.
            :param invocation_role: ``CfnServer.IdentityProviderDetailsProperty.InvocationRole``.
            :param url: ``CfnServer.IdentityProviderDetailsProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                identity_provider_details_property = transfer.CfnServer.IdentityProviderDetailsProperty(
                    directory_id="directoryId",
                    function="function",
                    invocation_role="invocationRole",
                    url="url"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if directory_id is not None:
                self._values["directory_id"] = directory_id
            if function is not None:
                self._values["function"] = function
            if invocation_role is not None:
                self._values["invocation_role"] = invocation_role
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def directory_id(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.IdentityProviderDetailsProperty.DirectoryId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-directoryid
            '''
            result = self._values.get("directory_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def function(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.IdentityProviderDetailsProperty.Function``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-function
            '''
            result = self._values.get("function")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def invocation_role(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.IdentityProviderDetailsProperty.InvocationRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-invocationrole
            '''
            result = self._values.get("invocation_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.IdentityProviderDetailsProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityProviderDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnServer.ProtocolDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"passive_ip": "passiveIp"},
    )
    class ProtocolDetailsProperty:
        def __init__(self, *, passive_ip: typing.Optional[builtins.str] = None) -> None:
            '''
            :param passive_ip: ``CfnServer.ProtocolDetailsProperty.PassiveIp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                protocol_details_property = transfer.CfnServer.ProtocolDetailsProperty(
                    passive_ip="passiveIp"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if passive_ip is not None:
                self._values["passive_ip"] = passive_ip

        @builtins.property
        def passive_ip(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.ProtocolDetailsProperty.PassiveIp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-passiveip
            '''
            result = self._values.get("passive_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtocolDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnServer.WorkflowDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"execution_role": "executionRole", "workflow_id": "workflowId"},
    )
    class WorkflowDetailProperty:
        def __init__(
            self,
            *,
            execution_role: builtins.str,
            workflow_id: builtins.str,
        ) -> None:
            '''
            :param execution_role: ``CfnServer.WorkflowDetailProperty.ExecutionRole``.
            :param workflow_id: ``CfnServer.WorkflowDetailProperty.WorkflowId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                workflow_detail_property = transfer.CfnServer.WorkflowDetailProperty(
                    execution_role="executionRole",
                    workflow_id="workflowId"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "execution_role": execution_role,
                "workflow_id": workflow_id,
            }

        @builtins.property
        def execution_role(self) -> builtins.str:
            '''``CfnServer.WorkflowDetailProperty.ExecutionRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-executionrole
            '''
            result = self._values.get("execution_role")
            assert result is not None, "Required property 'execution_role' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def workflow_id(self) -> builtins.str:
            '''``CfnServer.WorkflowDetailProperty.WorkflowId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-workflowid
            '''
            result = self._values.get("workflow_id")
            assert result is not None, "Required property 'workflow_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnServer.WorkflowDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"on_upload": "onUpload"},
    )
    class WorkflowDetailsProperty:
        def __init__(
            self,
            *,
            on_upload: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnServer.WorkflowDetailProperty", _IResolvable_a771d0ef]]],
        ) -> None:
            '''
            :param on_upload: ``CfnServer.WorkflowDetailsProperty.OnUpload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                workflow_details_property = transfer.CfnServer.WorkflowDetailsProperty(
                    on_upload=[transfer.CfnServer.WorkflowDetailProperty(
                        execution_role="executionRole",
                        workflow_id="workflowId"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "on_upload": on_upload,
            }

        @builtins.property
        def on_upload(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnServer.WorkflowDetailProperty", _IResolvable_a771d0ef]]]:
            '''``CfnServer.WorkflowDetailsProperty.OnUpload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html#cfn-transfer-server-workflowdetails-onupload
            '''
            result = self._values.get("on_upload")
            assert result is not None, "Required property 'on_upload' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnServer.WorkflowDetailProperty", _IResolvable_a771d0ef]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_transfer.CfnServerProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "domain": "domain",
        "endpoint_details": "endpointDetails",
        "endpoint_type": "endpointType",
        "identity_provider_details": "identityProviderDetails",
        "identity_provider_type": "identityProviderType",
        "logging_role": "loggingRole",
        "protocol_details": "protocolDetails",
        "protocols": "protocols",
        "security_policy_name": "securityPolicyName",
        "tags": "tags",
        "workflow_details": "workflowDetails",
    },
)
class CfnServerProps:
    def __init__(
        self,
        *,
        certificate: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        endpoint_details: typing.Optional[typing.Union[CfnServer.EndpointDetailsProperty, _IResolvable_a771d0ef]] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        identity_provider_details: typing.Optional[typing.Union[CfnServer.IdentityProviderDetailsProperty, _IResolvable_a771d0ef]] = None,
        identity_provider_type: typing.Optional[builtins.str] = None,
        logging_role: typing.Optional[builtins.str] = None,
        protocol_details: typing.Optional[typing.Union[CfnServer.ProtocolDetailsProperty, _IResolvable_a771d0ef]] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        workflow_details: typing.Optional[typing.Union[CfnServer.WorkflowDetailsProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Transfer::Server``.

        :param certificate: ``AWS::Transfer::Server.Certificate``.
        :param domain: ``AWS::Transfer::Server.Domain``.
        :param endpoint_details: ``AWS::Transfer::Server.EndpointDetails``.
        :param endpoint_type: ``AWS::Transfer::Server.EndpointType``.
        :param identity_provider_details: ``AWS::Transfer::Server.IdentityProviderDetails``.
        :param identity_provider_type: ``AWS::Transfer::Server.IdentityProviderType``.
        :param logging_role: ``AWS::Transfer::Server.LoggingRole``.
        :param protocol_details: ``AWS::Transfer::Server.ProtocolDetails``.
        :param protocols: ``AWS::Transfer::Server.Protocols``.
        :param security_policy_name: ``AWS::Transfer::Server.SecurityPolicyName``.
        :param tags: ``AWS::Transfer::Server.Tags``.
        :param workflow_details: ``AWS::Transfer::Server.WorkflowDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_transfer as transfer
            
            cfn_server_props = transfer.CfnServerProps(
                certificate="certificate",
                domain="domain",
                endpoint_details=transfer.CfnServer.EndpointDetailsProperty(
                    address_allocation_ids=["addressAllocationIds"],
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                ),
                endpoint_type="endpointType",
                identity_provider_details=transfer.CfnServer.IdentityProviderDetailsProperty(
                    directory_id="directoryId",
                    function="function",
                    invocation_role="invocationRole",
                    url="url"
                ),
                identity_provider_type="identityProviderType",
                logging_role="loggingRole",
                protocol_details=transfer.CfnServer.ProtocolDetailsProperty(
                    passive_ip="passiveIp"
                ),
                protocols=["protocols"],
                security_policy_name="securityPolicyName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                workflow_details=transfer.CfnServer.WorkflowDetailsProperty(
                    on_upload=[transfer.CfnServer.WorkflowDetailProperty(
                        execution_role="executionRole",
                        workflow_id="workflowId"
                    )]
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if certificate is not None:
            self._values["certificate"] = certificate
        if domain is not None:
            self._values["domain"] = domain
        if endpoint_details is not None:
            self._values["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            self._values["endpoint_type"] = endpoint_type
        if identity_provider_details is not None:
            self._values["identity_provider_details"] = identity_provider_details
        if identity_provider_type is not None:
            self._values["identity_provider_type"] = identity_provider_type
        if logging_role is not None:
            self._values["logging_role"] = logging_role
        if protocol_details is not None:
            self._values["protocol_details"] = protocol_details
        if protocols is not None:
            self._values["protocols"] = protocols
        if security_policy_name is not None:
            self._values["security_policy_name"] = security_policy_name
        if tags is not None:
            self._values["tags"] = tags
        if workflow_details is not None:
            self._values["workflow_details"] = workflow_details

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_details(
        self,
    ) -> typing.Optional[typing.Union[CfnServer.EndpointDetailsProperty, _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.EndpointDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails
        '''
        result = self._values.get("endpoint_details")
        return typing.cast(typing.Optional[typing.Union[CfnServer.EndpointDetailsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.EndpointType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype
        '''
        result = self._values.get("endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_details(
        self,
    ) -> typing.Optional[typing.Union[CfnServer.IdentityProviderDetailsProperty, _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.IdentityProviderDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails
        '''
        result = self._values.get("identity_provider_details")
        return typing.cast(typing.Optional[typing.Union[CfnServer.IdentityProviderDetailsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def identity_provider_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.IdentityProviderType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype
        '''
        result = self._values.get("identity_provider_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.LoggingRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole
        '''
        result = self._values.get("logging_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol_details(
        self,
    ) -> typing.Optional[typing.Union[CfnServer.ProtocolDetailsProperty, _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.ProtocolDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocoldetails
        '''
        result = self._values.get("protocol_details")
        return typing.cast(typing.Optional[typing.Union[CfnServer.ProtocolDetailsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::Server.Protocols``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocols
        '''
        result = self._values.get("protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.SecurityPolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-securitypolicyname
        '''
        result = self._values.get("security_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Transfer::Server.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def workflow_details(
        self,
    ) -> typing.Optional[typing.Union[CfnServer.WorkflowDetailsProperty, _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::Server.WorkflowDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-workflowdetails
        '''
        result = self._values.get("workflow_details")
        return typing.cast(typing.Optional[typing.Union[CfnServer.WorkflowDetailsProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnUser(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_transfer.CfnUser",
):
    '''A CloudFormation ``AWS::Transfer::User``.

    :cloudformationResource: AWS::Transfer::User
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_transfer as transfer
        
        cfn_user = transfer.CfnUser(self, "MyCfnUser",
            role="role",
            server_id="serverId",
            user_name="userName",
        
            # the properties below are optional
            home_directory="homeDirectory",
            home_directory_mappings=[transfer.CfnUser.HomeDirectoryMapEntryProperty(
                entry="entry",
                target="target"
            )],
            home_directory_type="homeDirectoryType",
            policy="policy",
            posix_profile=transfer.CfnUser.PosixProfileProperty(
                gid=123,
                uid=123,
        
                # the properties below are optional
                secondary_gids=[123]
            ),
            ssh_public_keys=["sshPublicKeys"],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnUser.HomeDirectoryMapEntryProperty", _IResolvable_a771d0ef]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union["CfnUser.PosixProfileProperty", _IResolvable_a771d0ef]] = None,
        role: builtins.str,
        server_id: builtins.str,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        user_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Transfer::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param home_directory: ``AWS::Transfer::User.HomeDirectory``.
        :param home_directory_mappings: ``AWS::Transfer::User.HomeDirectoryMappings``.
        :param home_directory_type: ``AWS::Transfer::User.HomeDirectoryType``.
        :param policy: ``AWS::Transfer::User.Policy``.
        :param posix_profile: ``AWS::Transfer::User.PosixProfile``.
        :param role: ``AWS::Transfer::User.Role``.
        :param server_id: ``AWS::Transfer::User.ServerId``.
        :param ssh_public_keys: ``AWS::Transfer::User.SshPublicKeys``.
        :param tags: ``AWS::Transfer::User.Tags``.
        :param user_name: ``AWS::Transfer::User.UserName``.
        '''
        props = CfnUserProps(
            home_directory=home_directory,
            home_directory_mappings=home_directory_mappings,
            home_directory_type=home_directory_type,
            policy=policy,
            posix_profile=posix_profile,
            role=role,
            server_id=server_id,
            ssh_public_keys=ssh_public_keys,
            tags=tags,
            user_name=user_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserName")
    def attr_user_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: UserName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeDirectory")
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectory"))

    @home_directory.setter
    def home_directory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "homeDirectory", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeDirectoryMappings")
    def home_directory_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnUser.HomeDirectoryMapEntryProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::Transfer::User.HomeDirectoryMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorymappings
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnUser.HomeDirectoryMapEntryProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "homeDirectoryMappings"))

    @home_directory_mappings.setter
    def home_directory_mappings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnUser.HomeDirectoryMapEntryProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "homeDirectoryMappings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeDirectoryType")
    def home_directory_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectoryType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorytype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectoryType"))

    @home_directory_type.setter
    def home_directory_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "homeDirectoryType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "policy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="posixProfile")
    def posix_profile(
        self,
    ) -> typing.Optional[typing.Union["CfnUser.PosixProfileProperty", _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::User.PosixProfile``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-posixprofile
        '''
        return typing.cast(typing.Optional[typing.Union["CfnUser.PosixProfileProperty", _IResolvable_a771d0ef]], jsii.get(self, "posixProfile"))

    @posix_profile.setter
    def posix_profile(
        self,
        value: typing.Optional[typing.Union["CfnUser.PosixProfileProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "posixProfile", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''``AWS::Transfer::User.Role``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
        '''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        jsii.set(self, "role", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        '''``AWS::Transfer::User.ServerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
        '''
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        jsii.set(self, "serverId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::User.SshPublicKeys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "sshPublicKeys", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Transfer::User.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''``AWS::Transfer::User.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
        '''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        jsii.set(self, "userName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnUser.HomeDirectoryMapEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"entry": "entry", "target": "target"},
    )
    class HomeDirectoryMapEntryProperty:
        def __init__(self, *, entry: builtins.str, target: builtins.str) -> None:
            '''
            :param entry: ``CfnUser.HomeDirectoryMapEntryProperty.Entry``.
            :param target: ``CfnUser.HomeDirectoryMapEntryProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                home_directory_map_entry_property = transfer.CfnUser.HomeDirectoryMapEntryProperty(
                    entry="entry",
                    target="target"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "entry": entry,
                "target": target,
            }

        @builtins.property
        def entry(self) -> builtins.str:
            '''``CfnUser.HomeDirectoryMapEntryProperty.Entry``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-entry
            '''
            result = self._values.get("entry")
            assert result is not None, "Required property 'entry' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''``CfnUser.HomeDirectoryMapEntryProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HomeDirectoryMapEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnUser.PosixProfileProperty",
        jsii_struct_bases=[],
        name_mapping={"gid": "gid", "secondary_gids": "secondaryGids", "uid": "uid"},
    )
    class PosixProfileProperty:
        def __init__(
            self,
            *,
            gid: jsii.Number,
            secondary_gids: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[jsii.Number]]] = None,
            uid: jsii.Number,
        ) -> None:
            '''
            :param gid: ``CfnUser.PosixProfileProperty.Gid``.
            :param secondary_gids: ``CfnUser.PosixProfileProperty.SecondaryGids``.
            :param uid: ``CfnUser.PosixProfileProperty.Uid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                posix_profile_property = transfer.CfnUser.PosixProfileProperty(
                    gid=123,
                    uid=123,
                
                    # the properties below are optional
                    secondary_gids=[123]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "gid": gid,
                "uid": uid,
            }
            if secondary_gids is not None:
                self._values["secondary_gids"] = secondary_gids

        @builtins.property
        def gid(self) -> jsii.Number:
            '''``CfnUser.PosixProfileProperty.Gid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-gid
            '''
            result = self._values.get("gid")
            assert result is not None, "Required property 'gid' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def secondary_gids(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]]:
            '''``CfnUser.PosixProfileProperty.SecondaryGids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-secondarygids
            '''
            result = self._values.get("secondary_gids")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]], result)

        @builtins.property
        def uid(self) -> jsii.Number:
            '''``CfnUser.PosixProfileProperty.Uid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-uid
            '''
            result = self._values.get("uid")
            assert result is not None, "Required property 'uid' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PosixProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_transfer.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "home_directory": "homeDirectory",
        "home_directory_mappings": "homeDirectoryMappings",
        "home_directory_type": "homeDirectoryType",
        "policy": "policy",
        "posix_profile": "posixProfile",
        "role": "role",
        "server_id": "serverId",
        "ssh_public_keys": "sshPublicKeys",
        "tags": "tags",
        "user_name": "userName",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnUser.HomeDirectoryMapEntryProperty, _IResolvable_a771d0ef]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union[CfnUser.PosixProfileProperty, _IResolvable_a771d0ef]] = None,
        role: builtins.str,
        server_id: builtins.str,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
        user_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::Transfer::User``.

        :param home_directory: ``AWS::Transfer::User.HomeDirectory``.
        :param home_directory_mappings: ``AWS::Transfer::User.HomeDirectoryMappings``.
        :param home_directory_type: ``AWS::Transfer::User.HomeDirectoryType``.
        :param policy: ``AWS::Transfer::User.Policy``.
        :param posix_profile: ``AWS::Transfer::User.PosixProfile``.
        :param role: ``AWS::Transfer::User.Role``.
        :param server_id: ``AWS::Transfer::User.ServerId``.
        :param ssh_public_keys: ``AWS::Transfer::User.SshPublicKeys``.
        :param tags: ``AWS::Transfer::User.Tags``.
        :param user_name: ``AWS::Transfer::User.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_transfer as transfer
            
            cfn_user_props = transfer.CfnUserProps(
                role="role",
                server_id="serverId",
                user_name="userName",
            
                # the properties below are optional
                home_directory="homeDirectory",
                home_directory_mappings=[transfer.CfnUser.HomeDirectoryMapEntryProperty(
                    entry="entry",
                    target="target"
                )],
                home_directory_type="homeDirectoryType",
                policy="policy",
                posix_profile=transfer.CfnUser.PosixProfileProperty(
                    gid=123,
                    uid=123,
            
                    # the properties below are optional
                    secondary_gids=[123]
                ),
                ssh_public_keys=["sshPublicKeys"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "role": role,
            "server_id": server_id,
            "user_name": user_name,
        }
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if home_directory_mappings is not None:
            self._values["home_directory_mappings"] = home_directory_mappings
        if home_directory_type is not None:
            self._values["home_directory_type"] = home_directory_type
        if policy is not None:
            self._values["policy"] = policy
        if posix_profile is not None:
            self._values["posix_profile"] = posix_profile
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
        '''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnUser.HomeDirectoryMapEntryProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::Transfer::User.HomeDirectoryMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorymappings
        '''
        result = self._values.get("home_directory_mappings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnUser.HomeDirectoryMapEntryProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def home_directory_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectoryType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorytype
        '''
        result = self._values.get("home_directory_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_profile(
        self,
    ) -> typing.Optional[typing.Union[CfnUser.PosixProfileProperty, _IResolvable_a771d0ef]]:
        '''``AWS::Transfer::User.PosixProfile``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-posixprofile
        '''
        result = self._values.get("posix_profile")
        return typing.cast(typing.Optional[typing.Union[CfnUser.PosixProfileProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def role(self) -> builtins.str:
        '''``AWS::Transfer::User.Role``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''``AWS::Transfer::User.ServerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
        '''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::User.SshPublicKeys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
        '''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Transfer::User.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''``AWS::Transfer::User.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnWorkflow(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_transfer.CfnWorkflow",
):
    '''A CloudFormation ``AWS::Transfer::Workflow``.

    :cloudformationResource: AWS::Transfer::Workflow
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_transfer as transfer
        
        # copy_step_details is of type object
        # custom_step_details is of type object
        # delete_step_details is of type object
        # tag_step_details is of type object
        
        cfn_workflow = transfer.CfnWorkflow(self, "MyCfnWorkflow",
            steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
                type="type"
            )],
        
            # the properties below are optional
            description="description",
            on_exception_steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
                type="type"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]]] = None,
        steps: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]],
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Create a new ``AWS::Transfer::Workflow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::Transfer::Workflow.Description``.
        :param on_exception_steps: ``AWS::Transfer::Workflow.OnExceptionSteps``.
        :param steps: ``AWS::Transfer::Workflow.Steps``.
        :param tags: ``AWS::Transfer::Workflow.Tags``.
        '''
        props = CfnWorkflowProps(
            description=description,
            on_exception_steps=on_exception_steps,
            steps=steps,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrWorkflowId")
    def attr_workflow_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: WorkflowId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkflowId"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Workflow.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onExceptionSteps")
    def on_exception_steps(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]]]:
        '''``AWS::Transfer::Workflow.OnExceptionSteps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-onexceptionsteps
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "onExceptionSteps"))

    @on_exception_steps.setter
    def on_exception_steps(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "onExceptionSteps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="steps")
    def steps(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]]:
        '''``AWS::Transfer::Workflow.Steps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-steps
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]], jsii.get(self, "steps"))

    @steps.setter
    def steps(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnWorkflow.WorkflowStepProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "steps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''``AWS::Transfer::Workflow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @jsii.data_type(
        jsii_type="monocdk.aws_transfer.CfnWorkflow.WorkflowStepProperty",
        jsii_struct_bases=[],
        name_mapping={
            "copy_step_details": "copyStepDetails",
            "custom_step_details": "customStepDetails",
            "delete_step_details": "deleteStepDetails",
            "tag_step_details": "tagStepDetails",
            "type": "type",
        },
    )
    class WorkflowStepProperty:
        def __init__(
            self,
            *,
            copy_step_details: typing.Any = None,
            custom_step_details: typing.Any = None,
            delete_step_details: typing.Any = None,
            tag_step_details: typing.Any = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param copy_step_details: ``CfnWorkflow.WorkflowStepProperty.CopyStepDetails``.
            :param custom_step_details: ``CfnWorkflow.WorkflowStepProperty.CustomStepDetails``.
            :param delete_step_details: ``CfnWorkflow.WorkflowStepProperty.DeleteStepDetails``.
            :param tag_step_details: ``CfnWorkflow.WorkflowStepProperty.TagStepDetails``.
            :param type: ``CfnWorkflow.WorkflowStepProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_transfer as transfer
                
                # copy_step_details is of type object
                # custom_step_details is of type object
                # delete_step_details is of type object
                # tag_step_details is of type object
                
                workflow_step_property = transfer.CfnWorkflow.WorkflowStepProperty(
                    copy_step_details=copy_step_details,
                    custom_step_details=custom_step_details,
                    delete_step_details=delete_step_details,
                    tag_step_details=tag_step_details,
                    type="type"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if copy_step_details is not None:
                self._values["copy_step_details"] = copy_step_details
            if custom_step_details is not None:
                self._values["custom_step_details"] = custom_step_details
            if delete_step_details is not None:
                self._values["delete_step_details"] = delete_step_details
            if tag_step_details is not None:
                self._values["tag_step_details"] = tag_step_details
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def copy_step_details(self) -> typing.Any:
            '''``CfnWorkflow.WorkflowStepProperty.CopyStepDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-copystepdetails
            '''
            result = self._values.get("copy_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def custom_step_details(self) -> typing.Any:
            '''``CfnWorkflow.WorkflowStepProperty.CustomStepDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-customstepdetails
            '''
            result = self._values.get("custom_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def delete_step_details(self) -> typing.Any:
            '''``CfnWorkflow.WorkflowStepProperty.DeleteStepDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-deletestepdetails
            '''
            result = self._values.get("delete_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def tag_step_details(self) -> typing.Any:
            '''``CfnWorkflow.WorkflowStepProperty.TagStepDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-tagstepdetails
            '''
            result = self._values.get("tag_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkflow.WorkflowStepProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowStepProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_transfer.CfnWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "on_exception_steps": "onExceptionSteps",
        "steps": "steps",
        "tags": "tags",
    },
)
class CfnWorkflowProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnWorkflow.WorkflowStepProperty, _IResolvable_a771d0ef]]]] = None,
        steps: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnWorkflow.WorkflowStepProperty, _IResolvable_a771d0ef]]],
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Transfer::Workflow``.

        :param description: ``AWS::Transfer::Workflow.Description``.
        :param on_exception_steps: ``AWS::Transfer::Workflow.OnExceptionSteps``.
        :param steps: ``AWS::Transfer::Workflow.Steps``.
        :param tags: ``AWS::Transfer::Workflow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_transfer as transfer
            
            # copy_step_details is of type object
            # custom_step_details is of type object
            # delete_step_details is of type object
            # tag_step_details is of type object
            
            cfn_workflow_props = transfer.CfnWorkflowProps(
                steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                    copy_step_details=copy_step_details,
                    custom_step_details=custom_step_details,
                    delete_step_details=delete_step_details,
                    tag_step_details=tag_step_details,
                    type="type"
                )],
            
                # the properties below are optional
                description="description",
                on_exception_steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                    copy_step_details=copy_step_details,
                    custom_step_details=custom_step_details,
                    delete_step_details=delete_step_details,
                    tag_step_details=tag_step_details,
                    type="type"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "steps": steps,
        }
        if description is not None:
            self._values["description"] = description
        if on_exception_steps is not None:
            self._values["on_exception_steps"] = on_exception_steps
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Workflow.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_exception_steps(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnWorkflow.WorkflowStepProperty, _IResolvable_a771d0ef]]]]:
        '''``AWS::Transfer::Workflow.OnExceptionSteps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-onexceptionsteps
        '''
        result = self._values.get("on_exception_steps")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnWorkflow.WorkflowStepProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def steps(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnWorkflow.WorkflowStepProperty, _IResolvable_a771d0ef]]]:
        '''``AWS::Transfer::Workflow.Steps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-steps
        '''
        result = self._values.get("steps")
        assert result is not None, "Required property 'steps' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnWorkflow.WorkflowStepProperty, _IResolvable_a771d0ef]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''``AWS::Transfer::Workflow.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnServer",
    "CfnServerProps",
    "CfnUser",
    "CfnUserProps",
    "CfnWorkflow",
    "CfnWorkflowProps",
]

publication.publish()
