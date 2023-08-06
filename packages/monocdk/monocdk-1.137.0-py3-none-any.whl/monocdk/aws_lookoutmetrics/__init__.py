'''
# AWS::LookoutMetrics Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as lookoutmetrics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LookoutMetrics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LookoutMetrics.html).

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
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnAlert(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lookoutmetrics.CfnAlert",
):
    '''A CloudFormation ``AWS::LookoutMetrics::Alert``.

    :cloudformationResource: AWS::LookoutMetrics::Alert
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_lookoutmetrics as lookoutmetrics
        
        cfn_alert = lookoutmetrics.CfnAlert(self, "MyCfnAlert",
            action=lookoutmetrics.CfnAlert.ActionProperty(
                lambda_configuration=lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                    lambda_arn="lambdaArn",
                    role_arn="roleArn"
                ),
                sns_configuration=lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                    role_arn="roleArn",
                    sns_topic_arn="snsTopicArn"
                )
            ),
            alert_sensitivity_threshold=123,
            anomaly_detector_arn="anomalyDetectorArn",
        
            # the properties below are optional
            alert_description="alertDescription",
            alert_name="alertName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        action: typing.Union["CfnAlert.ActionProperty", _IResolvable_a771d0ef],
        alert_description: typing.Optional[builtins.str] = None,
        alert_name: typing.Optional[builtins.str] = None,
        alert_sensitivity_threshold: jsii.Number,
        anomaly_detector_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::LookoutMetrics::Alert``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::LookoutMetrics::Alert.Action``.
        :param alert_description: ``AWS::LookoutMetrics::Alert.AlertDescription``.
        :param alert_name: ``AWS::LookoutMetrics::Alert.AlertName``.
        :param alert_sensitivity_threshold: ``AWS::LookoutMetrics::Alert.AlertSensitivityThreshold``.
        :param anomaly_detector_arn: ``AWS::LookoutMetrics::Alert.AnomalyDetectorArn``.
        '''
        props = CfnAlertProps(
            action=action,
            alert_description=alert_description,
            alert_name=alert_name,
            alert_sensitivity_threshold=alert_sensitivity_threshold,
            anomaly_detector_arn=anomaly_detector_arn,
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
    @jsii.member(jsii_name="action")
    def action(self) -> typing.Union["CfnAlert.ActionProperty", _IResolvable_a771d0ef]:
        '''``AWS::LookoutMetrics::Alert.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-action
        '''
        return typing.cast(typing.Union["CfnAlert.ActionProperty", _IResolvable_a771d0ef], jsii.get(self, "action"))

    @action.setter
    def action(
        self,
        value: typing.Union["CfnAlert.ActionProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "action", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alertDescription")
    def alert_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::Alert.AlertDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertDescription"))

    @alert_description.setter
    def alert_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "alertDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alertName")
    def alert_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::Alert.AlertName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertName"))

    @alert_name.setter
    def alert_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "alertName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alertSensitivityThreshold")
    def alert_sensitivity_threshold(self) -> jsii.Number:
        '''``AWS::LookoutMetrics::Alert.AlertSensitivityThreshold``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertsensitivitythreshold
        '''
        return typing.cast(jsii.Number, jsii.get(self, "alertSensitivityThreshold"))

    @alert_sensitivity_threshold.setter
    def alert_sensitivity_threshold(self, value: jsii.Number) -> None:
        jsii.set(self, "alertSensitivityThreshold", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="anomalyDetectorArn")
    def anomaly_detector_arn(self) -> builtins.str:
        '''``AWS::LookoutMetrics::Alert.AnomalyDetectorArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-anomalydetectorarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "anomalyDetectorArn"))

    @anomaly_detector_arn.setter
    def anomaly_detector_arn(self, value: builtins.str) -> None:
        jsii.set(self, "anomalyDetectorArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAlert.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_configuration": "lambdaConfiguration",
            "sns_configuration": "snsConfiguration",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            lambda_configuration: typing.Optional[typing.Union["CfnAlert.LambdaConfigurationProperty", _IResolvable_a771d0ef]] = None,
            sns_configuration: typing.Optional[typing.Union["CfnAlert.SNSConfigurationProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param lambda_configuration: ``CfnAlert.ActionProperty.LambdaConfiguration``.
            :param sns_configuration: ``CfnAlert.ActionProperty.SNSConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                action_property = lookoutmetrics.CfnAlert.ActionProperty(
                    lambda_configuration=lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                        lambda_arn="lambdaArn",
                        role_arn="roleArn"
                    ),
                    sns_configuration=lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                        role_arn="roleArn",
                        sns_topic_arn="snsTopicArn"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if lambda_configuration is not None:
                self._values["lambda_configuration"] = lambda_configuration
            if sns_configuration is not None:
                self._values["sns_configuration"] = sns_configuration

        @builtins.property
        def lambda_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnAlert.LambdaConfigurationProperty", _IResolvable_a771d0ef]]:
            '''``CfnAlert.ActionProperty.LambdaConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-lambdaconfiguration
            '''
            result = self._values.get("lambda_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnAlert.LambdaConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def sns_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnAlert.SNSConfigurationProperty", _IResolvable_a771d0ef]]:
            '''``CfnAlert.ActionProperty.SNSConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-snsconfiguration
            '''
            result = self._values.get("sns_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnAlert.SNSConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAlert.LambdaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_arn": "lambdaArn", "role_arn": "roleArn"},
    )
    class LambdaConfigurationProperty:
        def __init__(self, *, lambda_arn: builtins.str, role_arn: builtins.str) -> None:
            '''
            :param lambda_arn: ``CfnAlert.LambdaConfigurationProperty.LambdaArn``.
            :param role_arn: ``CfnAlert.LambdaConfigurationProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                lambda_configuration_property = lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                    lambda_arn="lambdaArn",
                    role_arn="roleArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "lambda_arn": lambda_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''``CfnAlert.LambdaConfigurationProperty.LambdaArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnAlert.LambdaConfigurationProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAlert.SNSConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "sns_topic_arn": "snsTopicArn"},
    )
    class SNSConfigurationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            sns_topic_arn: builtins.str,
        ) -> None:
            '''
            :param role_arn: ``CfnAlert.SNSConfigurationProperty.RoleArn``.
            :param sns_topic_arn: ``CfnAlert.SNSConfigurationProperty.SnsTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                s_nSConfiguration_property = lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                    role_arn="roleArn",
                    sns_topic_arn="snsTopicArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "sns_topic_arn": sns_topic_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnAlert.SNSConfigurationProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sns_topic_arn(self) -> builtins.str:
            '''``CfnAlert.SNSConfigurationProperty.SnsTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            assert result is not None, "Required property 'sns_topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SNSConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lookoutmetrics.CfnAlertProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "alert_description": "alertDescription",
        "alert_name": "alertName",
        "alert_sensitivity_threshold": "alertSensitivityThreshold",
        "anomaly_detector_arn": "anomalyDetectorArn",
    },
)
class CfnAlertProps:
    def __init__(
        self,
        *,
        action: typing.Union[CfnAlert.ActionProperty, _IResolvable_a771d0ef],
        alert_description: typing.Optional[builtins.str] = None,
        alert_name: typing.Optional[builtins.str] = None,
        alert_sensitivity_threshold: jsii.Number,
        anomaly_detector_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::LookoutMetrics::Alert``.

        :param action: ``AWS::LookoutMetrics::Alert.Action``.
        :param alert_description: ``AWS::LookoutMetrics::Alert.AlertDescription``.
        :param alert_name: ``AWS::LookoutMetrics::Alert.AlertName``.
        :param alert_sensitivity_threshold: ``AWS::LookoutMetrics::Alert.AlertSensitivityThreshold``.
        :param anomaly_detector_arn: ``AWS::LookoutMetrics::Alert.AnomalyDetectorArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_lookoutmetrics as lookoutmetrics
            
            cfn_alert_props = lookoutmetrics.CfnAlertProps(
                action=lookoutmetrics.CfnAlert.ActionProperty(
                    lambda_configuration=lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                        lambda_arn="lambdaArn",
                        role_arn="roleArn"
                    ),
                    sns_configuration=lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                        role_arn="roleArn",
                        sns_topic_arn="snsTopicArn"
                    )
                ),
                alert_sensitivity_threshold=123,
                anomaly_detector_arn="anomalyDetectorArn",
            
                # the properties below are optional
                alert_description="alertDescription",
                alert_name="alertName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "alert_sensitivity_threshold": alert_sensitivity_threshold,
            "anomaly_detector_arn": anomaly_detector_arn,
        }
        if alert_description is not None:
            self._values["alert_description"] = alert_description
        if alert_name is not None:
            self._values["alert_name"] = alert_name

    @builtins.property
    def action(self) -> typing.Union[CfnAlert.ActionProperty, _IResolvable_a771d0ef]:
        '''``AWS::LookoutMetrics::Alert.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(typing.Union[CfnAlert.ActionProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def alert_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::Alert.AlertDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertdescription
        '''
        result = self._values.get("alert_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alert_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::Alert.AlertName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertname
        '''
        result = self._values.get("alert_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alert_sensitivity_threshold(self) -> jsii.Number:
        '''``AWS::LookoutMetrics::Alert.AlertSensitivityThreshold``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertsensitivitythreshold
        '''
        result = self._values.get("alert_sensitivity_threshold")
        assert result is not None, "Required property 'alert_sensitivity_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def anomaly_detector_arn(self) -> builtins.str:
        '''``AWS::LookoutMetrics::Alert.AnomalyDetectorArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-anomalydetectorarn
        '''
        result = self._values.get("anomaly_detector_arn")
        assert result is not None, "Required property 'anomaly_detector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAlertProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnAnomalyDetector(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector",
):
    '''A CloudFormation ``AWS::LookoutMetrics::AnomalyDetector``.

    :cloudformationResource: AWS::LookoutMetrics::AnomalyDetector
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_lookoutmetrics as lookoutmetrics
        
        cfn_anomaly_detector = lookoutmetrics.CfnAnomalyDetector(self, "MyCfnAnomalyDetector",
            anomaly_detector_config=lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty(
                anomaly_detector_frequency="anomalyDetectorFrequency"
            ),
            metric_set_list=[lookoutmetrics.CfnAnomalyDetector.MetricSetProperty(
                metric_list=[lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                    aggregation_function="aggregationFunction",
                    metric_name="metricName",
        
                    # the properties below are optional
                    namespace="namespace"
                )],
                metric_set_name="metricSetName",
                metric_source=lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                    app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                        flow_name="flowName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                        role_arn="roleArn"
                    ),
                    rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        db_instance_identifier="dbInstanceIdentifier",
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                        cluster_identifier="clusterIdentifier",
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                        file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                            csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                charset="charset",
                                contains_header=False,
                                delimiter="delimiter",
                                file_compression="fileCompression",
                                header_list=["headerList"],
                                quote_symbol="quoteSymbol"
                            ),
                            json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                charset="charset",
                                file_compression="fileCompression"
                            )
                        ),
                        role_arn="roleArn",
        
                        # the properties below are optional
                        historical_data_path_list=["historicalDataPathList"],
                        templated_path_list=["templatedPathList"]
                    )
                ),
        
                # the properties below are optional
                dimension_list=["dimensionList"],
                metric_set_description="metricSetDescription",
                metric_set_frequency="metricSetFrequency",
                offset=123,
                timestamp_column=lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                    column_format="columnFormat",
                    column_name="columnName"
                ),
                timezone="timezone"
            )],
        
            # the properties below are optional
            anomaly_detector_description="anomalyDetectorDescription",
            anomaly_detector_name="anomalyDetectorName",
            kms_key_arn="kmsKeyArn"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        anomaly_detector_config: typing.Union["CfnAnomalyDetector.AnomalyDetectorConfigProperty", _IResolvable_a771d0ef],
        anomaly_detector_description: typing.Optional[builtins.str] = None,
        anomaly_detector_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        metric_set_list: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAnomalyDetector.MetricSetProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        '''Create a new ``AWS::LookoutMetrics::AnomalyDetector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param anomaly_detector_config: ``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig``.
        :param anomaly_detector_description: ``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorDescription``.
        :param anomaly_detector_name: ``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorName``.
        :param kms_key_arn: ``AWS::LookoutMetrics::AnomalyDetector.KmsKeyArn``.
        :param metric_set_list: ``AWS::LookoutMetrics::AnomalyDetector.MetricSetList``.
        '''
        props = CfnAnomalyDetectorProps(
            anomaly_detector_config=anomaly_detector_config,
            anomaly_detector_description=anomaly_detector_description,
            anomaly_detector_name=anomaly_detector_name,
            kms_key_arn=kms_key_arn,
            metric_set_list=metric_set_list,
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
    @jsii.member(jsii_name="anomalyDetectorConfig")
    def anomaly_detector_config(
        self,
    ) -> typing.Union["CfnAnomalyDetector.AnomalyDetectorConfigProperty", _IResolvable_a771d0ef]:
        '''``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig
        '''
        return typing.cast(typing.Union["CfnAnomalyDetector.AnomalyDetectorConfigProperty", _IResolvable_a771d0ef], jsii.get(self, "anomalyDetectorConfig"))

    @anomaly_detector_config.setter
    def anomaly_detector_config(
        self,
        value: typing.Union["CfnAnomalyDetector.AnomalyDetectorConfigProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "anomalyDetectorConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="anomalyDetectorDescription")
    def anomaly_detector_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectordescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "anomalyDetectorDescription"))

    @anomaly_detector_description.setter
    def anomaly_detector_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "anomalyDetectorDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="anomalyDetectorName")
    def anomaly_detector_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "anomalyDetectorName"))

    @anomaly_detector_name.setter
    def anomaly_detector_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "anomalyDetectorName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::AnomalyDetector.KmsKeyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-kmskeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricSetList")
    def metric_set_list(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.MetricSetProperty", _IResolvable_a771d0ef]]]:
        '''``AWS::LookoutMetrics::AnomalyDetector.MetricSetList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-metricsetlist
        '''
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.MetricSetProperty", _IResolvable_a771d0ef]]], jsii.get(self, "metricSetList"))

    @metric_set_list.setter
    def metric_set_list(
        self,
        value: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.MetricSetProperty", _IResolvable_a771d0ef]]],
    ) -> None:
        jsii.set(self, "metricSetList", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"anomaly_detector_frequency": "anomalyDetectorFrequency"},
    )
    class AnomalyDetectorConfigProperty:
        def __init__(self, *, anomaly_detector_frequency: builtins.str) -> None:
            '''
            :param anomaly_detector_frequency: ``CfnAnomalyDetector.AnomalyDetectorConfigProperty.AnomalyDetectorFrequency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                anomaly_detector_config_property = lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty(
                    anomaly_detector_frequency="anomalyDetectorFrequency"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "anomaly_detector_frequency": anomaly_detector_frequency,
            }

        @builtins.property
        def anomaly_detector_frequency(self) -> builtins.str:
            '''``CfnAnomalyDetector.AnomalyDetectorConfigProperty.AnomalyDetectorFrequency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig-anomalydetectorfrequency
            '''
            result = self._values.get("anomaly_detector_frequency")
            assert result is not None, "Required property 'anomaly_detector_frequency' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnomalyDetectorConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"flow_name": "flowName", "role_arn": "roleArn"},
    )
    class AppFlowConfigProperty:
        def __init__(self, *, flow_name: builtins.str, role_arn: builtins.str) -> None:
            '''
            :param flow_name: ``CfnAnomalyDetector.AppFlowConfigProperty.FlowName``.
            :param role_arn: ``CfnAnomalyDetector.AppFlowConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                app_flow_config_property = lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                    flow_name="flowName",
                    role_arn="roleArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "flow_name": flow_name,
                "role_arn": role_arn,
            }

        @builtins.property
        def flow_name(self) -> builtins.str:
            '''``CfnAnomalyDetector.AppFlowConfigProperty.FlowName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-flowname
            '''
            result = self._values.get("flow_name")
            assert result is not None, "Required property 'flow_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnAnomalyDetector.AppFlowConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppFlowConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn"},
    )
    class CloudwatchConfigProperty:
        def __init__(self, *, role_arn: builtins.str) -> None:
            '''
            :param role_arn: ``CfnAnomalyDetector.CloudwatchConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                cloudwatch_config_property = lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                    role_arn="roleArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnAnomalyDetector.CloudwatchConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html#cfn-lookoutmetrics-anomalydetector-cloudwatchconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "charset": "charset",
            "contains_header": "containsHeader",
            "delimiter": "delimiter",
            "file_compression": "fileCompression",
            "header_list": "headerList",
            "quote_symbol": "quoteSymbol",
        },
    )
    class CsvFormatDescriptorProperty:
        def __init__(
            self,
            *,
            charset: typing.Optional[builtins.str] = None,
            contains_header: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            delimiter: typing.Optional[builtins.str] = None,
            file_compression: typing.Optional[builtins.str] = None,
            header_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            quote_symbol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param charset: ``CfnAnomalyDetector.CsvFormatDescriptorProperty.Charset``.
            :param contains_header: ``CfnAnomalyDetector.CsvFormatDescriptorProperty.ContainsHeader``.
            :param delimiter: ``CfnAnomalyDetector.CsvFormatDescriptorProperty.Delimiter``.
            :param file_compression: ``CfnAnomalyDetector.CsvFormatDescriptorProperty.FileCompression``.
            :param header_list: ``CfnAnomalyDetector.CsvFormatDescriptorProperty.HeaderList``.
            :param quote_symbol: ``CfnAnomalyDetector.CsvFormatDescriptorProperty.QuoteSymbol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                csv_format_descriptor_property = lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                    charset="charset",
                    contains_header=False,
                    delimiter="delimiter",
                    file_compression="fileCompression",
                    header_list=["headerList"],
                    quote_symbol="quoteSymbol"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if charset is not None:
                self._values["charset"] = charset
            if contains_header is not None:
                self._values["contains_header"] = contains_header
            if delimiter is not None:
                self._values["delimiter"] = delimiter
            if file_compression is not None:
                self._values["file_compression"] = file_compression
            if header_list is not None:
                self._values["header_list"] = header_list
            if quote_symbol is not None:
                self._values["quote_symbol"] = quote_symbol

        @builtins.property
        def charset(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.CsvFormatDescriptorProperty.Charset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-charset
            '''
            result = self._values.get("charset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def contains_header(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.CsvFormatDescriptorProperty.ContainsHeader``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-containsheader
            '''
            result = self._values.get("contains_header")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.CsvFormatDescriptorProperty.Delimiter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_compression(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.CsvFormatDescriptorProperty.FileCompression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-filecompression
            '''
            result = self._values.get("file_compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def header_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAnomalyDetector.CsvFormatDescriptorProperty.HeaderList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-headerlist
            '''
            result = self._values.get("header_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def quote_symbol(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.CsvFormatDescriptorProperty.QuoteSymbol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-quotesymbol
            '''
            result = self._values.get("quote_symbol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsvFormatDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_format_descriptor": "csvFormatDescriptor",
            "json_format_descriptor": "jsonFormatDescriptor",
        },
    )
    class FileFormatDescriptorProperty:
        def __init__(
            self,
            *,
            csv_format_descriptor: typing.Optional[typing.Union["CfnAnomalyDetector.CsvFormatDescriptorProperty", _IResolvable_a771d0ef]] = None,
            json_format_descriptor: typing.Optional[typing.Union["CfnAnomalyDetector.JsonFormatDescriptorProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param csv_format_descriptor: ``CfnAnomalyDetector.FileFormatDescriptorProperty.CsvFormatDescriptor``.
            :param json_format_descriptor: ``CfnAnomalyDetector.FileFormatDescriptorProperty.JsonFormatDescriptor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                file_format_descriptor_property = lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                    csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                        charset="charset",
                        contains_header=False,
                        delimiter="delimiter",
                        file_compression="fileCompression",
                        header_list=["headerList"],
                        quote_symbol="quoteSymbol"
                    ),
                    json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                        charset="charset",
                        file_compression="fileCompression"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if csv_format_descriptor is not None:
                self._values["csv_format_descriptor"] = csv_format_descriptor
            if json_format_descriptor is not None:
                self._values["json_format_descriptor"] = json_format_descriptor

        @builtins.property
        def csv_format_descriptor(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.CsvFormatDescriptorProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.FileFormatDescriptorProperty.CsvFormatDescriptor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-csvformatdescriptor
            '''
            result = self._values.get("csv_format_descriptor")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.CsvFormatDescriptorProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def json_format_descriptor(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.JsonFormatDescriptorProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.FileFormatDescriptorProperty.JsonFormatDescriptor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-jsonformatdescriptor
            '''
            result = self._values.get("json_format_descriptor")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.JsonFormatDescriptorProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileFormatDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={"charset": "charset", "file_compression": "fileCompression"},
    )
    class JsonFormatDescriptorProperty:
        def __init__(
            self,
            *,
            charset: typing.Optional[builtins.str] = None,
            file_compression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param charset: ``CfnAnomalyDetector.JsonFormatDescriptorProperty.Charset``.
            :param file_compression: ``CfnAnomalyDetector.JsonFormatDescriptorProperty.FileCompression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                json_format_descriptor_property = lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                    charset="charset",
                    file_compression="fileCompression"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if charset is not None:
                self._values["charset"] = charset
            if file_compression is not None:
                self._values["file_compression"] = file_compression

        @builtins.property
        def charset(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.JsonFormatDescriptorProperty.Charset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-charset
            '''
            result = self._values.get("charset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_compression(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.JsonFormatDescriptorProperty.FileCompression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-filecompression
            '''
            result = self._values.get("file_compression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonFormatDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation_function": "aggregationFunction",
            "metric_name": "metricName",
            "namespace": "namespace",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            aggregation_function: builtins.str,
            metric_name: builtins.str,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param aggregation_function: ``CfnAnomalyDetector.MetricProperty.AggregationFunction``.
            :param metric_name: ``CfnAnomalyDetector.MetricProperty.MetricName``.
            :param namespace: ``CfnAnomalyDetector.MetricProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                metric_property = lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                    aggregation_function="aggregationFunction",
                    metric_name="metricName",
                
                    # the properties below are optional
                    namespace="namespace"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "aggregation_function": aggregation_function,
                "metric_name": metric_name,
            }
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def aggregation_function(self) -> builtins.str:
            '''``CfnAnomalyDetector.MetricProperty.AggregationFunction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-aggregationfunction
            '''
            result = self._values.get("aggregation_function")
            assert result is not None, "Required property 'aggregation_function' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''``CfnAnomalyDetector.MetricProperty.MetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.MetricProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.MetricSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimension_list": "dimensionList",
            "metric_list": "metricList",
            "metric_set_description": "metricSetDescription",
            "metric_set_frequency": "metricSetFrequency",
            "metric_set_name": "metricSetName",
            "metric_source": "metricSource",
            "offset": "offset",
            "timestamp_column": "timestampColumn",
            "timezone": "timezone",
        },
    )
    class MetricSetProperty:
        def __init__(
            self,
            *,
            dimension_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            metric_list: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAnomalyDetector.MetricProperty", _IResolvable_a771d0ef]]],
            metric_set_description: typing.Optional[builtins.str] = None,
            metric_set_frequency: typing.Optional[builtins.str] = None,
            metric_set_name: builtins.str,
            metric_source: typing.Union["CfnAnomalyDetector.MetricSourceProperty", _IResolvable_a771d0ef],
            offset: typing.Optional[jsii.Number] = None,
            timestamp_column: typing.Optional[typing.Union["CfnAnomalyDetector.TimestampColumnProperty", _IResolvable_a771d0ef]] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dimension_list: ``CfnAnomalyDetector.MetricSetProperty.DimensionList``.
            :param metric_list: ``CfnAnomalyDetector.MetricSetProperty.MetricList``.
            :param metric_set_description: ``CfnAnomalyDetector.MetricSetProperty.MetricSetDescription``.
            :param metric_set_frequency: ``CfnAnomalyDetector.MetricSetProperty.MetricSetFrequency``.
            :param metric_set_name: ``CfnAnomalyDetector.MetricSetProperty.MetricSetName``.
            :param metric_source: ``CfnAnomalyDetector.MetricSetProperty.MetricSource``.
            :param offset: ``CfnAnomalyDetector.MetricSetProperty.Offset``.
            :param timestamp_column: ``CfnAnomalyDetector.MetricSetProperty.TimestampColumn``.
            :param timezone: ``CfnAnomalyDetector.MetricSetProperty.Timezone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                metric_set_property = lookoutmetrics.CfnAnomalyDetector.MetricSetProperty(
                    metric_list=[lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                        aggregation_function="aggregationFunction",
                        metric_name="metricName",
                
                        # the properties below are optional
                        namespace="namespace"
                    )],
                    metric_set_name="metricSetName",
                    metric_source=lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                        app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                            flow_name="flowName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                            role_arn="roleArn"
                        ),
                        rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            db_instance_identifier="dbInstanceIdentifier",
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                            cluster_identifier="clusterIdentifier",
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                            file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                                csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                    charset="charset",
                                    contains_header=False,
                                    delimiter="delimiter",
                                    file_compression="fileCompression",
                                    header_list=["headerList"],
                                    quote_symbol="quoteSymbol"
                                ),
                                json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                    charset="charset",
                                    file_compression="fileCompression"
                                )
                            ),
                            role_arn="roleArn",
                
                            # the properties below are optional
                            historical_data_path_list=["historicalDataPathList"],
                            templated_path_list=["templatedPathList"]
                        )
                    ),
                
                    # the properties below are optional
                    dimension_list=["dimensionList"],
                    metric_set_description="metricSetDescription",
                    metric_set_frequency="metricSetFrequency",
                    offset=123,
                    timestamp_column=lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                        column_format="columnFormat",
                        column_name="columnName"
                    ),
                    timezone="timezone"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric_list": metric_list,
                "metric_set_name": metric_set_name,
                "metric_source": metric_source,
            }
            if dimension_list is not None:
                self._values["dimension_list"] = dimension_list
            if metric_set_description is not None:
                self._values["metric_set_description"] = metric_set_description
            if metric_set_frequency is not None:
                self._values["metric_set_frequency"] = metric_set_frequency
            if offset is not None:
                self._values["offset"] = offset
            if timestamp_column is not None:
                self._values["timestamp_column"] = timestamp_column
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def dimension_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAnomalyDetector.MetricSetProperty.DimensionList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-dimensionlist
            '''
            result = self._values.get("dimension_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def metric_list(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.MetricProperty", _IResolvable_a771d0ef]]]:
            '''``CfnAnomalyDetector.MetricSetProperty.MetricList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metriclist
            '''
            result = self._values.get("metric_list")
            assert result is not None, "Required property 'metric_list' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.MetricProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def metric_set_description(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.MetricSetProperty.MetricSetDescription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetdescription
            '''
            result = self._values.get("metric_set_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_set_frequency(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.MetricSetProperty.MetricSetFrequency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetfrequency
            '''
            result = self._values.get("metric_set_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_set_name(self) -> builtins.str:
            '''``CfnAnomalyDetector.MetricSetProperty.MetricSetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetname
            '''
            result = self._values.get("metric_set_name")
            assert result is not None, "Required property 'metric_set_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_source(
            self,
        ) -> typing.Union["CfnAnomalyDetector.MetricSourceProperty", _IResolvable_a771d0ef]:
            '''``CfnAnomalyDetector.MetricSetProperty.MetricSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsource
            '''
            result = self._values.get("metric_source")
            assert result is not None, "Required property 'metric_source' is missing"
            return typing.cast(typing.Union["CfnAnomalyDetector.MetricSourceProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def offset(self) -> typing.Optional[jsii.Number]:
            '''``CfnAnomalyDetector.MetricSetProperty.Offset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-offset
            '''
            result = self._values.get("offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timestamp_column(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.TimestampColumnProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.MetricSetProperty.TimestampColumn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timestampcolumn
            '''
            result = self._values.get("timestamp_column")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.TimestampColumnProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.MetricSetProperty.Timezone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_flow_config": "appFlowConfig",
            "cloudwatch_config": "cloudwatchConfig",
            "rds_source_config": "rdsSourceConfig",
            "redshift_source_config": "redshiftSourceConfig",
            "s3_source_config": "s3SourceConfig",
        },
    )
    class MetricSourceProperty:
        def __init__(
            self,
            *,
            app_flow_config: typing.Optional[typing.Union["CfnAnomalyDetector.AppFlowConfigProperty", _IResolvable_a771d0ef]] = None,
            cloudwatch_config: typing.Optional[typing.Union["CfnAnomalyDetector.CloudwatchConfigProperty", _IResolvable_a771d0ef]] = None,
            rds_source_config: typing.Optional[typing.Union["CfnAnomalyDetector.RDSSourceConfigProperty", _IResolvable_a771d0ef]] = None,
            redshift_source_config: typing.Optional[typing.Union["CfnAnomalyDetector.RedshiftSourceConfigProperty", _IResolvable_a771d0ef]] = None,
            s3_source_config: typing.Optional[typing.Union["CfnAnomalyDetector.S3SourceConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''
            :param app_flow_config: ``CfnAnomalyDetector.MetricSourceProperty.AppFlowConfig``.
            :param cloudwatch_config: ``CfnAnomalyDetector.MetricSourceProperty.CloudwatchConfig``.
            :param rds_source_config: ``CfnAnomalyDetector.MetricSourceProperty.RDSSourceConfig``.
            :param redshift_source_config: ``CfnAnomalyDetector.MetricSourceProperty.RedshiftSourceConfig``.
            :param s3_source_config: ``CfnAnomalyDetector.MetricSourceProperty.S3SourceConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                metric_source_property = lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                    app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                        flow_name="flowName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                        role_arn="roleArn"
                    ),
                    rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        db_instance_identifier="dbInstanceIdentifier",
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                        cluster_identifier="clusterIdentifier",
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                        file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                            csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                charset="charset",
                                contains_header=False,
                                delimiter="delimiter",
                                file_compression="fileCompression",
                                header_list=["headerList"],
                                quote_symbol="quoteSymbol"
                            ),
                            json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                charset="charset",
                                file_compression="fileCompression"
                            )
                        ),
                        role_arn="roleArn",
                
                        # the properties below are optional
                        historical_data_path_list=["historicalDataPathList"],
                        templated_path_list=["templatedPathList"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if app_flow_config is not None:
                self._values["app_flow_config"] = app_flow_config
            if cloudwatch_config is not None:
                self._values["cloudwatch_config"] = cloudwatch_config
            if rds_source_config is not None:
                self._values["rds_source_config"] = rds_source_config
            if redshift_source_config is not None:
                self._values["redshift_source_config"] = redshift_source_config
            if s3_source_config is not None:
                self._values["s3_source_config"] = s3_source_config

        @builtins.property
        def app_flow_config(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.AppFlowConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.MetricSourceProperty.AppFlowConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-appflowconfig
            '''
            result = self._values.get("app_flow_config")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.AppFlowConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def cloudwatch_config(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.CloudwatchConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.MetricSourceProperty.CloudwatchConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-cloudwatchconfig
            '''
            result = self._values.get("cloudwatch_config")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.CloudwatchConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def rds_source_config(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.RDSSourceConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.MetricSourceProperty.RDSSourceConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-rdssourceconfig
            '''
            result = self._values.get("rds_source_config")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.RDSSourceConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def redshift_source_config(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.RedshiftSourceConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.MetricSourceProperty.RedshiftSourceConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-redshiftsourceconfig
            '''
            result = self._values.get("redshift_source_config")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.RedshiftSourceConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def s3_source_config(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.S3SourceConfigProperty", _IResolvable_a771d0ef]]:
            '''``CfnAnomalyDetector.MetricSourceProperty.S3SourceConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-s3sourceconfig
            '''
            result = self._values.get("s3_source_config")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.S3SourceConfigProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_host": "databaseHost",
            "database_name": "databaseName",
            "database_port": "databasePort",
            "db_instance_identifier": "dbInstanceIdentifier",
            "role_arn": "roleArn",
            "secret_manager_arn": "secretManagerArn",
            "table_name": "tableName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class RDSSourceConfigProperty:
        def __init__(
            self,
            *,
            database_host: builtins.str,
            database_name: builtins.str,
            database_port: jsii.Number,
            db_instance_identifier: builtins.str,
            role_arn: builtins.str,
            secret_manager_arn: builtins.str,
            table_name: builtins.str,
            vpc_configuration: typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param database_host: ``CfnAnomalyDetector.RDSSourceConfigProperty.DatabaseHost``.
            :param database_name: ``CfnAnomalyDetector.RDSSourceConfigProperty.DatabaseName``.
            :param database_port: ``CfnAnomalyDetector.RDSSourceConfigProperty.DatabasePort``.
            :param db_instance_identifier: ``CfnAnomalyDetector.RDSSourceConfigProperty.DBInstanceIdentifier``.
            :param role_arn: ``CfnAnomalyDetector.RDSSourceConfigProperty.RoleArn``.
            :param secret_manager_arn: ``CfnAnomalyDetector.RDSSourceConfigProperty.SecretManagerArn``.
            :param table_name: ``CfnAnomalyDetector.RDSSourceConfigProperty.TableName``.
            :param vpc_configuration: ``CfnAnomalyDetector.RDSSourceConfigProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                r_dSSource_config_property = lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                    database_host="databaseHost",
                    database_name="databaseName",
                    database_port=123,
                    db_instance_identifier="dbInstanceIdentifier",
                    role_arn="roleArn",
                    secret_manager_arn="secretManagerArn",
                    table_name="tableName",
                    vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                        security_group_id_list=["securityGroupIdList"],
                        subnet_id_list=["subnetIdList"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database_host": database_host,
                "database_name": database_name,
                "database_port": database_port,
                "db_instance_identifier": db_instance_identifier,
                "role_arn": role_arn,
                "secret_manager_arn": secret_manager_arn,
                "table_name": table_name,
                "vpc_configuration": vpc_configuration,
            }

        @builtins.property
        def database_host(self) -> builtins.str:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.DatabaseHost``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasehost
            '''
            result = self._values.get("database_host")
            assert result is not None, "Required property 'database_host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_port(self) -> jsii.Number:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.DatabasePort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databaseport
            '''
            result = self._values.get("database_port")
            assert result is not None, "Required property 'database_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def db_instance_identifier(self) -> builtins.str:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.DBInstanceIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-dbinstanceidentifier
            '''
            result = self._values.get("db_instance_identifier")
            assert result is not None, "Required property 'db_instance_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_manager_arn(self) -> builtins.str:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.SecretManagerArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            assert result is not None, "Required property 'secret_manager_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", _IResolvable_a771d0ef]:
            '''``CfnAnomalyDetector.RDSSourceConfigProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            assert result is not None, "Required property 'vpc_configuration' is missing"
            return typing.cast(typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RDSSourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_identifier": "clusterIdentifier",
            "database_host": "databaseHost",
            "database_name": "databaseName",
            "database_port": "databasePort",
            "role_arn": "roleArn",
            "secret_manager_arn": "secretManagerArn",
            "table_name": "tableName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class RedshiftSourceConfigProperty:
        def __init__(
            self,
            *,
            cluster_identifier: builtins.str,
            database_host: builtins.str,
            database_name: builtins.str,
            database_port: jsii.Number,
            role_arn: builtins.str,
            secret_manager_arn: builtins.str,
            table_name: builtins.str,
            vpc_configuration: typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", _IResolvable_a771d0ef],
        ) -> None:
            '''
            :param cluster_identifier: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.ClusterIdentifier``.
            :param database_host: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.DatabaseHost``.
            :param database_name: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.DatabaseName``.
            :param database_port: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.DatabasePort``.
            :param role_arn: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.RoleArn``.
            :param secret_manager_arn: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.SecretManagerArn``.
            :param table_name: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.TableName``.
            :param vpc_configuration: ``CfnAnomalyDetector.RedshiftSourceConfigProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                redshift_source_config_property = lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                    cluster_identifier="clusterIdentifier",
                    database_host="databaseHost",
                    database_name="databaseName",
                    database_port=123,
                    role_arn="roleArn",
                    secret_manager_arn="secretManagerArn",
                    table_name="tableName",
                    vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                        security_group_id_list=["securityGroupIdList"],
                        subnet_id_list=["subnetIdList"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_identifier": cluster_identifier,
                "database_host": database_host,
                "database_name": database_name,
                "database_port": database_port,
                "role_arn": role_arn,
                "secret_manager_arn": secret_manager_arn,
                "table_name": table_name,
                "vpc_configuration": vpc_configuration,
            }

        @builtins.property
        def cluster_identifier(self) -> builtins.str:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.ClusterIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-clusteridentifier
            '''
            result = self._values.get("cluster_identifier")
            assert result is not None, "Required property 'cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_host(self) -> builtins.str:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.DatabaseHost``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasehost
            '''
            result = self._values.get("database_host")
            assert result is not None, "Required property 'database_host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_port(self) -> jsii.Number:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.DatabasePort``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databaseport
            '''
            result = self._values.get("database_port")
            assert result is not None, "Required property 'database_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_manager_arn(self) -> builtins.str:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.SecretManagerArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            assert result is not None, "Required property 'secret_manager_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", _IResolvable_a771d0ef]:
            '''``CfnAnomalyDetector.RedshiftSourceConfigProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            assert result is not None, "Required property 'vpc_configuration' is missing"
            return typing.cast(typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftSourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "file_format_descriptor": "fileFormatDescriptor",
            "historical_data_path_list": "historicalDataPathList",
            "role_arn": "roleArn",
            "templated_path_list": "templatedPathList",
        },
    )
    class S3SourceConfigProperty:
        def __init__(
            self,
            *,
            file_format_descriptor: typing.Union["CfnAnomalyDetector.FileFormatDescriptorProperty", _IResolvable_a771d0ef],
            historical_data_path_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            role_arn: builtins.str,
            templated_path_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param file_format_descriptor: ``CfnAnomalyDetector.S3SourceConfigProperty.FileFormatDescriptor``.
            :param historical_data_path_list: ``CfnAnomalyDetector.S3SourceConfigProperty.HistoricalDataPathList``.
            :param role_arn: ``CfnAnomalyDetector.S3SourceConfigProperty.RoleArn``.
            :param templated_path_list: ``CfnAnomalyDetector.S3SourceConfigProperty.TemplatedPathList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                s3_source_config_property = lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                    file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                        csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                            charset="charset",
                            contains_header=False,
                            delimiter="delimiter",
                            file_compression="fileCompression",
                            header_list=["headerList"],
                            quote_symbol="quoteSymbol"
                        ),
                        json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                            charset="charset",
                            file_compression="fileCompression"
                        )
                    ),
                    role_arn="roleArn",
                
                    # the properties below are optional
                    historical_data_path_list=["historicalDataPathList"],
                    templated_path_list=["templatedPathList"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "file_format_descriptor": file_format_descriptor,
                "role_arn": role_arn,
            }
            if historical_data_path_list is not None:
                self._values["historical_data_path_list"] = historical_data_path_list
            if templated_path_list is not None:
                self._values["templated_path_list"] = templated_path_list

        @builtins.property
        def file_format_descriptor(
            self,
        ) -> typing.Union["CfnAnomalyDetector.FileFormatDescriptorProperty", _IResolvable_a771d0ef]:
            '''``CfnAnomalyDetector.S3SourceConfigProperty.FileFormatDescriptor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-fileformatdescriptor
            '''
            result = self._values.get("file_format_descriptor")
            assert result is not None, "Required property 'file_format_descriptor' is missing"
            return typing.cast(typing.Union["CfnAnomalyDetector.FileFormatDescriptorProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def historical_data_path_list(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAnomalyDetector.S3SourceConfigProperty.HistoricalDataPathList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-historicaldatapathlist
            '''
            result = self._values.get("historical_data_path_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnAnomalyDetector.S3SourceConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def templated_path_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAnomalyDetector.S3SourceConfigProperty.TemplatedPathList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-templatedpathlist
            '''
            result = self._values.get("templated_path_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column_format": "columnFormat", "column_name": "columnName"},
    )
    class TimestampColumnProperty:
        def __init__(
            self,
            *,
            column_format: typing.Optional[builtins.str] = None,
            column_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param column_format: ``CfnAnomalyDetector.TimestampColumnProperty.ColumnFormat``.
            :param column_name: ``CfnAnomalyDetector.TimestampColumnProperty.ColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                timestamp_column_property = lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                    column_format="columnFormat",
                    column_name="columnName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if column_format is not None:
                self._values["column_format"] = column_format
            if column_name is not None:
                self._values["column_name"] = column_name

        @builtins.property
        def column_format(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.TimestampColumnProperty.ColumnFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnformat
            '''
            result = self._values.get("column_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_name(self) -> typing.Optional[builtins.str]:
            '''``CfnAnomalyDetector.TimestampColumnProperty.ColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnname
            '''
            result = self._values.get("column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestampColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_id_list": "securityGroupIdList",
            "subnet_id_list": "subnetIdList",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_id_list: typing.Sequence[builtins.str],
            subnet_id_list: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_id_list: ``CfnAnomalyDetector.VpcConfigurationProperty.SecurityGroupIdList``.
            :param subnet_id_list: ``CfnAnomalyDetector.VpcConfigurationProperty.SubnetIdList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_lookoutmetrics as lookoutmetrics
                
                vpc_configuration_property = lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                    security_group_id_list=["securityGroupIdList"],
                    subnet_id_list=["subnetIdList"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_id_list": security_group_id_list,
                "subnet_id_list": subnet_id_list,
            }

        @builtins.property
        def security_group_id_list(self) -> typing.List[builtins.str]:
            '''``CfnAnomalyDetector.VpcConfigurationProperty.SecurityGroupIdList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-securitygroupidlist
            '''
            result = self._values.get("security_group_id_list")
            assert result is not None, "Required property 'security_group_id_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_id_list(self) -> typing.List[builtins.str]:
            '''``CfnAnomalyDetector.VpcConfigurationProperty.SubnetIdList``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-subnetidlist
            '''
            result = self._values.get("subnet_id_list")
            assert result is not None, "Required property 'subnet_id_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_lookoutmetrics.CfnAnomalyDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "anomaly_detector_config": "anomalyDetectorConfig",
        "anomaly_detector_description": "anomalyDetectorDescription",
        "anomaly_detector_name": "anomalyDetectorName",
        "kms_key_arn": "kmsKeyArn",
        "metric_set_list": "metricSetList",
    },
)
class CfnAnomalyDetectorProps:
    def __init__(
        self,
        *,
        anomaly_detector_config: typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigProperty, _IResolvable_a771d0ef],
        anomaly_detector_description: typing.Optional[builtins.str] = None,
        anomaly_detector_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        metric_set_list: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnAnomalyDetector.MetricSetProperty, _IResolvable_a771d0ef]]],
    ) -> None:
        '''Properties for defining a ``AWS::LookoutMetrics::AnomalyDetector``.

        :param anomaly_detector_config: ``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig``.
        :param anomaly_detector_description: ``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorDescription``.
        :param anomaly_detector_name: ``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorName``.
        :param kms_key_arn: ``AWS::LookoutMetrics::AnomalyDetector.KmsKeyArn``.
        :param metric_set_list: ``AWS::LookoutMetrics::AnomalyDetector.MetricSetList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_lookoutmetrics as lookoutmetrics
            
            cfn_anomaly_detector_props = lookoutmetrics.CfnAnomalyDetectorProps(
                anomaly_detector_config=lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty(
                    anomaly_detector_frequency="anomalyDetectorFrequency"
                ),
                metric_set_list=[lookoutmetrics.CfnAnomalyDetector.MetricSetProperty(
                    metric_list=[lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                        aggregation_function="aggregationFunction",
                        metric_name="metricName",
            
                        # the properties below are optional
                        namespace="namespace"
                    )],
                    metric_set_name="metricSetName",
                    metric_source=lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                        app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                            flow_name="flowName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                            role_arn="roleArn"
                        ),
                        rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            db_instance_identifier="dbInstanceIdentifier",
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                            cluster_identifier="clusterIdentifier",
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                            file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                                csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                    charset="charset",
                                    contains_header=False,
                                    delimiter="delimiter",
                                    file_compression="fileCompression",
                                    header_list=["headerList"],
                                    quote_symbol="quoteSymbol"
                                ),
                                json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                    charset="charset",
                                    file_compression="fileCompression"
                                )
                            ),
                            role_arn="roleArn",
            
                            # the properties below are optional
                            historical_data_path_list=["historicalDataPathList"],
                            templated_path_list=["templatedPathList"]
                        )
                    ),
            
                    # the properties below are optional
                    dimension_list=["dimensionList"],
                    metric_set_description="metricSetDescription",
                    metric_set_frequency="metricSetFrequency",
                    offset=123,
                    timestamp_column=lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                        column_format="columnFormat",
                        column_name="columnName"
                    ),
                    timezone="timezone"
                )],
            
                # the properties below are optional
                anomaly_detector_description="anomalyDetectorDescription",
                anomaly_detector_name="anomalyDetectorName",
                kms_key_arn="kmsKeyArn"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "anomaly_detector_config": anomaly_detector_config,
            "metric_set_list": metric_set_list,
        }
        if anomaly_detector_description is not None:
            self._values["anomaly_detector_description"] = anomaly_detector_description
        if anomaly_detector_name is not None:
            self._values["anomaly_detector_name"] = anomaly_detector_name
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def anomaly_detector_config(
        self,
    ) -> typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigProperty, _IResolvable_a771d0ef]:
        '''``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig
        '''
        result = self._values.get("anomaly_detector_config")
        assert result is not None, "Required property 'anomaly_detector_config' is missing"
        return typing.cast(typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def anomaly_detector_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectordescription
        '''
        result = self._values.get("anomaly_detector_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def anomaly_detector_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorname
        '''
        result = self._values.get("anomaly_detector_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::LookoutMetrics::AnomalyDetector.KmsKeyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_set_list(
        self,
    ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnomalyDetector.MetricSetProperty, _IResolvable_a771d0ef]]]:
        '''``AWS::LookoutMetrics::AnomalyDetector.MetricSetList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-metricsetlist
        '''
        result = self._values.get("metric_set_list")
        assert result is not None, "Required property 'metric_set_list' is missing"
        return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnomalyDetector.MetricSetProperty, _IResolvable_a771d0ef]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnomalyDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAlert",
    "CfnAlertProps",
    "CfnAnomalyDetector",
    "CfnAnomalyDetectorProps",
]

publication.publish()
