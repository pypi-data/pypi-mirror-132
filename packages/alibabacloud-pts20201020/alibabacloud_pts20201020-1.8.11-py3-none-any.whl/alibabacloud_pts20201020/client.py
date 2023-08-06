# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pts20201020 import models as pts20201020_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('pts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_pts_scene_with_options(
        self,
        request: pts20201020_models.CreatePtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.CreatePtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneResponse(),
            self.do_rpcrequest('CreatePtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_pts_scene_with_options_async(
        self,
        request: pts20201020_models.CreatePtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.CreatePtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneResponse(),
            await self.do_rpcrequest_async('CreatePtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pts_scene(
        self,
        request: pts20201020_models.CreatePtsSceneRequest,
    ) -> pts20201020_models.CreatePtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pts_scene_with_options(request, runtime)

    async def create_pts_scene_async(
        self,
        request: pts20201020_models.CreatePtsSceneRequest,
    ) -> pts20201020_models.CreatePtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pts_scene_with_options_async(request, runtime)

    def create_pts_scene_base_line_from_report_with_options(
        self,
        request: pts20201020_models.CreatePtsSceneBaseLineFromReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.CreatePtsSceneBaseLineFromReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneBaseLineFromReportResponse(),
            self.do_rpcrequest('CreatePtsSceneBaseLineFromReport', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_pts_scene_base_line_from_report_with_options_async(
        self,
        request: pts20201020_models.CreatePtsSceneBaseLineFromReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.CreatePtsSceneBaseLineFromReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneBaseLineFromReportResponse(),
            await self.do_rpcrequest_async('CreatePtsSceneBaseLineFromReport', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pts_scene_base_line_from_report(
        self,
        request: pts20201020_models.CreatePtsSceneBaseLineFromReportRequest,
    ) -> pts20201020_models.CreatePtsSceneBaseLineFromReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pts_scene_base_line_from_report_with_options(request, runtime)

    async def create_pts_scene_base_line_from_report_async(
        self,
        request: pts20201020_models.CreatePtsSceneBaseLineFromReportRequest,
    ) -> pts20201020_models.CreatePtsSceneBaseLineFromReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pts_scene_base_line_from_report_with_options_async(request, runtime)

    def delete_pts_scene_with_options(
        self,
        request: pts20201020_models.DeletePtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.DeletePtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneResponse(),
            self.do_rpcrequest('DeletePtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_pts_scene_with_options_async(
        self,
        request: pts20201020_models.DeletePtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.DeletePtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneResponse(),
            await self.do_rpcrequest_async('DeletePtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pts_scene(
        self,
        request: pts20201020_models.DeletePtsSceneRequest,
    ) -> pts20201020_models.DeletePtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scene_with_options(request, runtime)

    async def delete_pts_scene_async(
        self,
        request: pts20201020_models.DeletePtsSceneRequest,
    ) -> pts20201020_models.DeletePtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pts_scene_with_options_async(request, runtime)

    def delete_pts_scene_base_line_with_options(
        self,
        request: pts20201020_models.DeletePtsSceneBaseLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.DeletePtsSceneBaseLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneBaseLineResponse(),
            self.do_rpcrequest('DeletePtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_pts_scene_base_line_with_options_async(
        self,
        request: pts20201020_models.DeletePtsSceneBaseLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.DeletePtsSceneBaseLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneBaseLineResponse(),
            await self.do_rpcrequest_async('DeletePtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pts_scene_base_line(
        self,
        request: pts20201020_models.DeletePtsSceneBaseLineRequest,
    ) -> pts20201020_models.DeletePtsSceneBaseLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scene_base_line_with_options(request, runtime)

    async def delete_pts_scene_base_line_async(
        self,
        request: pts20201020_models.DeletePtsSceneBaseLineRequest,
    ) -> pts20201020_models.DeletePtsSceneBaseLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pts_scene_base_line_with_options_async(request, runtime)

    def delete_pts_scenes_with_options(
        self,
        tmp_req: pts20201020_models.DeletePtsScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.DeletePtsScenesResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.DeletePtsScenesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_ids):
            request.scene_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_ids, 'SceneIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsScenesResponse(),
            self.do_rpcrequest('DeletePtsScenes', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_pts_scenes_with_options_async(
        self,
        tmp_req: pts20201020_models.DeletePtsScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.DeletePtsScenesResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.DeletePtsScenesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_ids):
            request.scene_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_ids, 'SceneIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsScenesResponse(),
            await self.do_rpcrequest_async('DeletePtsScenes', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pts_scenes(
        self,
        request: pts20201020_models.DeletePtsScenesRequest,
    ) -> pts20201020_models.DeletePtsScenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scenes_with_options(request, runtime)

    async def delete_pts_scenes_async(
        self,
        request: pts20201020_models.DeletePtsScenesRequest,
    ) -> pts20201020_models.DeletePtsScenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pts_scenes_with_options_async(request, runtime)

    def get_jmeter_logs_with_options(
        self,
        request: pts20201020_models.GetJMeterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterLogsResponse(),
            self.do_rpcrequest('GetJMeterLogs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_jmeter_logs_with_options_async(
        self,
        request: pts20201020_models.GetJMeterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterLogsResponse(),
            await self.do_rpcrequest_async('GetJMeterLogs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_logs(
        self,
        request: pts20201020_models.GetJMeterLogsRequest,
    ) -> pts20201020_models.GetJMeterLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_logs_with_options(request, runtime)

    async def get_jmeter_logs_async(
        self,
        request: pts20201020_models.GetJMeterLogsRequest,
    ) -> pts20201020_models.GetJMeterLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_jmeter_logs_with_options_async(request, runtime)

    def get_jmeter_sample_metrics_with_options(
        self,
        request: pts20201020_models.GetJMeterSampleMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterSampleMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSampleMetricsResponse(),
            self.do_rpcrequest('GetJMeterSampleMetrics', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_jmeter_sample_metrics_with_options_async(
        self,
        request: pts20201020_models.GetJMeterSampleMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterSampleMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSampleMetricsResponse(),
            await self.do_rpcrequest_async('GetJMeterSampleMetrics', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_sample_metrics(
        self,
        request: pts20201020_models.GetJMeterSampleMetricsRequest,
    ) -> pts20201020_models.GetJMeterSampleMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_sample_metrics_with_options(request, runtime)

    async def get_jmeter_sample_metrics_async(
        self,
        request: pts20201020_models.GetJMeterSampleMetricsRequest,
    ) -> pts20201020_models.GetJMeterSampleMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_jmeter_sample_metrics_with_options_async(request, runtime)

    def get_jmeter_sampling_logs_with_options(
        self,
        request: pts20201020_models.GetJMeterSamplingLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterSamplingLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSamplingLogsResponse(),
            self.do_rpcrequest('GetJMeterSamplingLogs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_jmeter_sampling_logs_with_options_async(
        self,
        request: pts20201020_models.GetJMeterSamplingLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterSamplingLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSamplingLogsResponse(),
            await self.do_rpcrequest_async('GetJMeterSamplingLogs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_sampling_logs(
        self,
        request: pts20201020_models.GetJMeterSamplingLogsRequest,
    ) -> pts20201020_models.GetJMeterSamplingLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_sampling_logs_with_options(request, runtime)

    async def get_jmeter_sampling_logs_async(
        self,
        request: pts20201020_models.GetJMeterSamplingLogsRequest,
    ) -> pts20201020_models.GetJMeterSamplingLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_jmeter_sampling_logs_with_options_async(request, runtime)

    def get_jmeter_scene_running_data_with_options(
        self,
        request: pts20201020_models.GetJMeterSceneRunningDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterSceneRunningDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSceneRunningDataResponse(),
            self.do_rpcrequest('GetJMeterSceneRunningData', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_jmeter_scene_running_data_with_options_async(
        self,
        request: pts20201020_models.GetJMeterSceneRunningDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetJMeterSceneRunningDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSceneRunningDataResponse(),
            await self.do_rpcrequest_async('GetJMeterSceneRunningData', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_scene_running_data(
        self,
        request: pts20201020_models.GetJMeterSceneRunningDataRequest,
    ) -> pts20201020_models.GetJMeterSceneRunningDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_scene_running_data_with_options(request, runtime)

    async def get_jmeter_scene_running_data_async(
        self,
        request: pts20201020_models.GetJMeterSceneRunningDataRequest,
    ) -> pts20201020_models.GetJMeterSceneRunningDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_jmeter_scene_running_data_with_options_async(request, runtime)

    def get_open_jmeter_scene_with_options(
        self,
        request: pts20201020_models.GetOpenJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetOpenJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetOpenJMeterSceneResponse(),
            self.do_rpcrequest('GetOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_open_jmeter_scene_with_options_async(
        self,
        request: pts20201020_models.GetOpenJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetOpenJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetOpenJMeterSceneResponse(),
            await self.do_rpcrequest_async('GetOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_open_jmeter_scene(
        self,
        request: pts20201020_models.GetOpenJMeterSceneRequest,
    ) -> pts20201020_models.GetOpenJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_open_jmeter_scene_with_options(request, runtime)

    async def get_open_jmeter_scene_async(
        self,
        request: pts20201020_models.GetOpenJMeterSceneRequest,
    ) -> pts20201020_models.GetOpenJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_open_jmeter_scene_with_options_async(request, runtime)

    def get_pts_report_details_with_options(
        self,
        request: pts20201020_models.GetPtsReportDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsReportDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportDetailsResponse(),
            self.do_rpcrequest('GetPtsReportDetails', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pts_report_details_with_options_async(
        self,
        request: pts20201020_models.GetPtsReportDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsReportDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportDetailsResponse(),
            await self.do_rpcrequest_async('GetPtsReportDetails', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_report_details(
        self,
        request: pts20201020_models.GetPtsReportDetailsRequest,
    ) -> pts20201020_models.GetPtsReportDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pts_report_details_with_options(request, runtime)

    async def get_pts_report_details_async(
        self,
        request: pts20201020_models.GetPtsReportDetailsRequest,
    ) -> pts20201020_models.GetPtsReportDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pts_report_details_with_options_async(request, runtime)

    def get_pts_reports_by_scene_id_with_options(
        self,
        request: pts20201020_models.GetPtsReportsBySceneIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsReportsBySceneIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportsBySceneIdResponse(),
            self.do_rpcrequest('GetPtsReportsBySceneId', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pts_reports_by_scene_id_with_options_async(
        self,
        request: pts20201020_models.GetPtsReportsBySceneIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsReportsBySceneIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportsBySceneIdResponse(),
            await self.do_rpcrequest_async('GetPtsReportsBySceneId', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_reports_by_scene_id(
        self,
        request: pts20201020_models.GetPtsReportsBySceneIdRequest,
    ) -> pts20201020_models.GetPtsReportsBySceneIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pts_reports_by_scene_id_with_options(request, runtime)

    async def get_pts_reports_by_scene_id_async(
        self,
        request: pts20201020_models.GetPtsReportsBySceneIdRequest,
    ) -> pts20201020_models.GetPtsReportsBySceneIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pts_reports_by_scene_id_with_options_async(request, runtime)

    def get_pts_scene_with_options(
        self,
        request: pts20201020_models.GetPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneResponse(),
            self.do_rpcrequest('GetPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pts_scene_with_options_async(
        self,
        request: pts20201020_models.GetPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneResponse(),
            await self.do_rpcrequest_async('GetPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene(
        self,
        request: pts20201020_models.GetPtsSceneRequest,
    ) -> pts20201020_models.GetPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_with_options(request, runtime)

    async def get_pts_scene_async(
        self,
        request: pts20201020_models.GetPtsSceneRequest,
    ) -> pts20201020_models.GetPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pts_scene_with_options_async(request, runtime)

    def get_pts_scene_base_line_with_options(
        self,
        request: pts20201020_models.GetPtsSceneBaseLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneBaseLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneBaseLineResponse(),
            self.do_rpcrequest('GetPtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pts_scene_base_line_with_options_async(
        self,
        request: pts20201020_models.GetPtsSceneBaseLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneBaseLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneBaseLineResponse(),
            await self.do_rpcrequest_async('GetPtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene_base_line(
        self,
        request: pts20201020_models.GetPtsSceneBaseLineRequest,
    ) -> pts20201020_models.GetPtsSceneBaseLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_base_line_with_options(request, runtime)

    async def get_pts_scene_base_line_async(
        self,
        request: pts20201020_models.GetPtsSceneBaseLineRequest,
    ) -> pts20201020_models.GetPtsSceneBaseLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pts_scene_base_line_with_options_async(request, runtime)

    def get_pts_scene_running_data_with_options(
        self,
        request: pts20201020_models.GetPtsSceneRunningDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneRunningDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningDataResponse(),
            self.do_rpcrequest('GetPtsSceneRunningData', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pts_scene_running_data_with_options_async(
        self,
        request: pts20201020_models.GetPtsSceneRunningDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneRunningDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningDataResponse(),
            await self.do_rpcrequest_async('GetPtsSceneRunningData', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene_running_data(
        self,
        request: pts20201020_models.GetPtsSceneRunningDataRequest,
    ) -> pts20201020_models.GetPtsSceneRunningDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_running_data_with_options(request, runtime)

    async def get_pts_scene_running_data_async(
        self,
        request: pts20201020_models.GetPtsSceneRunningDataRequest,
    ) -> pts20201020_models.GetPtsSceneRunningDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pts_scene_running_data_with_options_async(request, runtime)

    def get_pts_scene_running_status_with_options(
        self,
        request: pts20201020_models.GetPtsSceneRunningStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneRunningStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningStatusResponse(),
            self.do_rpcrequest('GetPtsSceneRunningStatus', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pts_scene_running_status_with_options_async(
        self,
        request: pts20201020_models.GetPtsSceneRunningStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.GetPtsSceneRunningStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningStatusResponse(),
            await self.do_rpcrequest_async('GetPtsSceneRunningStatus', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene_running_status(
        self,
        request: pts20201020_models.GetPtsSceneRunningStatusRequest,
    ) -> pts20201020_models.GetPtsSceneRunningStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_running_status_with_options(request, runtime)

    async def get_pts_scene_running_status_async(
        self,
        request: pts20201020_models.GetPtsSceneRunningStatusRequest,
    ) -> pts20201020_models.GetPtsSceneRunningStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pts_scene_running_status_with_options_async(request, runtime)

    def list_envs_with_options(
        self,
        request: pts20201020_models.ListEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListEnvsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListEnvsResponse(),
            self.do_rpcrequest('ListEnvs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_envs_with_options_async(
        self,
        request: pts20201020_models.ListEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListEnvsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListEnvsResponse(),
            await self.do_rpcrequest_async('ListEnvs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_envs(
        self,
        request: pts20201020_models.ListEnvsRequest,
    ) -> pts20201020_models.ListEnvsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_envs_with_options(request, runtime)

    async def list_envs_async(
        self,
        request: pts20201020_models.ListEnvsRequest,
    ) -> pts20201020_models.ListEnvsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_envs_with_options_async(request, runtime)

    def list_jmeter_reports_with_options(
        self,
        request: pts20201020_models.ListJMeterReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListJMeterReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListJMeterReportsResponse(),
            self.do_rpcrequest('ListJMeterReports', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_jmeter_reports_with_options_async(
        self,
        request: pts20201020_models.ListJMeterReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListJMeterReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListJMeterReportsResponse(),
            await self.do_rpcrequest_async('ListJMeterReports', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jmeter_reports(
        self,
        request: pts20201020_models.ListJMeterReportsRequest,
    ) -> pts20201020_models.ListJMeterReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jmeter_reports_with_options(request, runtime)

    async def list_jmeter_reports_async(
        self,
        request: pts20201020_models.ListJMeterReportsRequest,
    ) -> pts20201020_models.ListJMeterReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jmeter_reports_with_options_async(request, runtime)

    def list_open_jmeter_scenes_with_options(
        self,
        request: pts20201020_models.ListOpenJMeterScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListOpenJMeterScenesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListOpenJMeterScenesResponse(),
            self.do_rpcrequest('ListOpenJMeterScenes', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_open_jmeter_scenes_with_options_async(
        self,
        request: pts20201020_models.ListOpenJMeterScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListOpenJMeterScenesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListOpenJMeterScenesResponse(),
            await self.do_rpcrequest_async('ListOpenJMeterScenes', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_open_jmeter_scenes(
        self,
        request: pts20201020_models.ListOpenJMeterScenesRequest,
    ) -> pts20201020_models.ListOpenJMeterScenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_open_jmeter_scenes_with_options(request, runtime)

    async def list_open_jmeter_scenes_async(
        self,
        request: pts20201020_models.ListOpenJMeterScenesRequest,
    ) -> pts20201020_models.ListOpenJMeterScenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_open_jmeter_scenes_with_options_async(request, runtime)

    def list_pts_scene_with_options(
        self,
        request: pts20201020_models.ListPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListPtsSceneResponse(),
            self.do_rpcrequest('ListPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_pts_scene_with_options_async(
        self,
        request: pts20201020_models.ListPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ListPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListPtsSceneResponse(),
            await self.do_rpcrequest_async('ListPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pts_scene(
        self,
        request: pts20201020_models.ListPtsSceneRequest,
    ) -> pts20201020_models.ListPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_pts_scene_with_options(request, runtime)

    async def list_pts_scene_async(
        self,
        request: pts20201020_models.ListPtsSceneRequest,
    ) -> pts20201020_models.ListPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_pts_scene_with_options_async(request, runtime)

    def modify_pts_scene_with_options(
        self,
        request: pts20201020_models.ModifyPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ModifyPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ModifyPtsSceneResponse(),
            self.do_rpcrequest('ModifyPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_pts_scene_with_options_async(
        self,
        request: pts20201020_models.ModifyPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.ModifyPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ModifyPtsSceneResponse(),
            await self.do_rpcrequest_async('ModifyPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_pts_scene(
        self,
        request: pts20201020_models.ModifyPtsSceneRequest,
    ) -> pts20201020_models.ModifyPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_pts_scene_with_options(request, runtime)

    async def modify_pts_scene_async(
        self,
        request: pts20201020_models.ModifyPtsSceneRequest,
    ) -> pts20201020_models.ModifyPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_pts_scene_with_options_async(request, runtime)

    def remove_env_with_options(
        self,
        request: pts20201020_models.RemoveEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.RemoveEnvResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveEnvResponse(),
            self.do_rpcrequest('RemoveEnv', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_env_with_options_async(
        self,
        request: pts20201020_models.RemoveEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.RemoveEnvResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveEnvResponse(),
            await self.do_rpcrequest_async('RemoveEnv', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_env(
        self,
        request: pts20201020_models.RemoveEnvRequest,
    ) -> pts20201020_models.RemoveEnvResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_env_with_options(request, runtime)

    async def remove_env_async(
        self,
        request: pts20201020_models.RemoveEnvRequest,
    ) -> pts20201020_models.RemoveEnvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_env_with_options_async(request, runtime)

    def remove_open_jmeter_scene_with_options(
        self,
        request: pts20201020_models.RemoveOpenJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.RemoveOpenJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveOpenJMeterSceneResponse(),
            self.do_rpcrequest('RemoveOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_open_jmeter_scene_with_options_async(
        self,
        request: pts20201020_models.RemoveOpenJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.RemoveOpenJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveOpenJMeterSceneResponse(),
            await self.do_rpcrequest_async('RemoveOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_open_jmeter_scene(
        self,
        request: pts20201020_models.RemoveOpenJMeterSceneRequest,
    ) -> pts20201020_models.RemoveOpenJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_open_jmeter_scene_with_options(request, runtime)

    async def remove_open_jmeter_scene_async(
        self,
        request: pts20201020_models.RemoveOpenJMeterSceneRequest,
    ) -> pts20201020_models.RemoveOpenJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_open_jmeter_scene_with_options_async(request, runtime)

    def save_env_with_options(
        self,
        tmp_req: pts20201020_models.SaveEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.SaveEnvResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveEnvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env):
            request.env_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.env), 'Env', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.SaveEnvResponse(),
            self.do_rpcrequest('SaveEnv', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_env_with_options_async(
        self,
        tmp_req: pts20201020_models.SaveEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.SaveEnvResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveEnvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env):
            request.env_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.env), 'Env', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.SaveEnvResponse(),
            await self.do_rpcrequest_async('SaveEnv', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_env(
        self,
        request: pts20201020_models.SaveEnvRequest,
    ) -> pts20201020_models.SaveEnvResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_env_with_options(request, runtime)

    async def save_env_async(
        self,
        request: pts20201020_models.SaveEnvRequest,
    ) -> pts20201020_models.SaveEnvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_env_with_options_async(request, runtime)

    def save_open_jmeter_scene_with_options(
        self,
        tmp_req: pts20201020_models.SaveOpenJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.SaveOpenJMeterSceneResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveOpenJMeterSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.open_jmeter_scene):
            request.open_jmeter_scene_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_jmeter_scene), 'OpenJMeterScene', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.SaveOpenJMeterSceneResponse(),
            self.do_rpcrequest('SaveOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_open_jmeter_scene_with_options_async(
        self,
        tmp_req: pts20201020_models.SaveOpenJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.SaveOpenJMeterSceneResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveOpenJMeterSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.open_jmeter_scene):
            request.open_jmeter_scene_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_jmeter_scene), 'OpenJMeterScene', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.SaveOpenJMeterSceneResponse(),
            await self.do_rpcrequest_async('SaveOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_open_jmeter_scene(
        self,
        request: pts20201020_models.SaveOpenJMeterSceneRequest,
    ) -> pts20201020_models.SaveOpenJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_open_jmeter_scene_with_options(request, runtime)

    async def save_open_jmeter_scene_async(
        self,
        request: pts20201020_models.SaveOpenJMeterSceneRequest,
    ) -> pts20201020_models.SaveOpenJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_open_jmeter_scene_with_options_async(request, runtime)

    def start_debug_pts_scene_with_options(
        self,
        request: pts20201020_models.StartDebugPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartDebugPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebugPtsSceneResponse(),
            self.do_rpcrequest('StartDebugPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_debug_pts_scene_with_options_async(
        self,
        request: pts20201020_models.StartDebugPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartDebugPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebugPtsSceneResponse(),
            await self.do_rpcrequest_async('StartDebugPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_debug_pts_scene(
        self,
        request: pts20201020_models.StartDebugPtsSceneRequest,
    ) -> pts20201020_models.StartDebugPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_debug_pts_scene_with_options(request, runtime)

    async def start_debug_pts_scene_async(
        self,
        request: pts20201020_models.StartDebugPtsSceneRequest,
    ) -> pts20201020_models.StartDebugPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_debug_pts_scene_with_options_async(request, runtime)

    def start_debugging_jmeter_scene_with_options(
        self,
        request: pts20201020_models.StartDebuggingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartDebuggingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebuggingJMeterSceneResponse(),
            self.do_rpcrequest('StartDebuggingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_debugging_jmeter_scene_with_options_async(
        self,
        request: pts20201020_models.StartDebuggingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartDebuggingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebuggingJMeterSceneResponse(),
            await self.do_rpcrequest_async('StartDebuggingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_debugging_jmeter_scene(
        self,
        request: pts20201020_models.StartDebuggingJMeterSceneRequest,
    ) -> pts20201020_models.StartDebuggingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_debugging_jmeter_scene_with_options(request, runtime)

    async def start_debugging_jmeter_scene_async(
        self,
        request: pts20201020_models.StartDebuggingJMeterSceneRequest,
    ) -> pts20201020_models.StartDebuggingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_debugging_jmeter_scene_with_options_async(request, runtime)

    def start_pts_scene_with_options(
        self,
        request: pts20201020_models.StartPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartPtsSceneResponse(),
            self.do_rpcrequest('StartPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_pts_scene_with_options_async(
        self,
        request: pts20201020_models.StartPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartPtsSceneResponse(),
            await self.do_rpcrequest_async('StartPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_pts_scene(
        self,
        request: pts20201020_models.StartPtsSceneRequest,
    ) -> pts20201020_models.StartPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_pts_scene_with_options(request, runtime)

    async def start_pts_scene_async(
        self,
        request: pts20201020_models.StartPtsSceneRequest,
    ) -> pts20201020_models.StartPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_pts_scene_with_options_async(request, runtime)

    def start_testing_jmeter_scene_with_options(
        self,
        request: pts20201020_models.StartTestingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartTestingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartTestingJMeterSceneResponse(),
            self.do_rpcrequest('StartTestingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_testing_jmeter_scene_with_options_async(
        self,
        request: pts20201020_models.StartTestingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StartTestingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartTestingJMeterSceneResponse(),
            await self.do_rpcrequest_async('StartTestingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_testing_jmeter_scene(
        self,
        request: pts20201020_models.StartTestingJMeterSceneRequest,
    ) -> pts20201020_models.StartTestingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_testing_jmeter_scene_with_options(request, runtime)

    async def start_testing_jmeter_scene_async(
        self,
        request: pts20201020_models.StartTestingJMeterSceneRequest,
    ) -> pts20201020_models.StartTestingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_testing_jmeter_scene_with_options_async(request, runtime)

    def stop_debug_pts_scene_with_options(
        self,
        request: pts20201020_models.StopDebugPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopDebugPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebugPtsSceneResponse(),
            self.do_rpcrequest('StopDebugPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_debug_pts_scene_with_options_async(
        self,
        request: pts20201020_models.StopDebugPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopDebugPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebugPtsSceneResponse(),
            await self.do_rpcrequest_async('StopDebugPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_debug_pts_scene(
        self,
        request: pts20201020_models.StopDebugPtsSceneRequest,
    ) -> pts20201020_models.StopDebugPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_debug_pts_scene_with_options(request, runtime)

    async def stop_debug_pts_scene_async(
        self,
        request: pts20201020_models.StopDebugPtsSceneRequest,
    ) -> pts20201020_models.StopDebugPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_debug_pts_scene_with_options_async(request, runtime)

    def stop_debugging_jmeter_scene_with_options(
        self,
        request: pts20201020_models.StopDebuggingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopDebuggingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebuggingJMeterSceneResponse(),
            self.do_rpcrequest('StopDebuggingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_debugging_jmeter_scene_with_options_async(
        self,
        request: pts20201020_models.StopDebuggingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopDebuggingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebuggingJMeterSceneResponse(),
            await self.do_rpcrequest_async('StopDebuggingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_debugging_jmeter_scene(
        self,
        request: pts20201020_models.StopDebuggingJMeterSceneRequest,
    ) -> pts20201020_models.StopDebuggingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_debugging_jmeter_scene_with_options(request, runtime)

    async def stop_debugging_jmeter_scene_async(
        self,
        request: pts20201020_models.StopDebuggingJMeterSceneRequest,
    ) -> pts20201020_models.StopDebuggingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_debugging_jmeter_scene_with_options_async(request, runtime)

    def stop_pts_scene_with_options(
        self,
        request: pts20201020_models.StopPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopPtsSceneResponse(),
            self.do_rpcrequest('StopPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_pts_scene_with_options_async(
        self,
        request: pts20201020_models.StopPtsSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopPtsSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopPtsSceneResponse(),
            await self.do_rpcrequest_async('StopPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_pts_scene(
        self,
        request: pts20201020_models.StopPtsSceneRequest,
    ) -> pts20201020_models.StopPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_pts_scene_with_options(request, runtime)

    async def stop_pts_scene_async(
        self,
        request: pts20201020_models.StopPtsSceneRequest,
    ) -> pts20201020_models.StopPtsSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_pts_scene_with_options_async(request, runtime)

    def stop_testing_jmeter_scene_with_options(
        self,
        request: pts20201020_models.StopTestingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopTestingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopTestingJMeterSceneResponse(),
            self.do_rpcrequest('StopTestingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_testing_jmeter_scene_with_options_async(
        self,
        request: pts20201020_models.StopTestingJMeterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.StopTestingJMeterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopTestingJMeterSceneResponse(),
            await self.do_rpcrequest_async('StopTestingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_testing_jmeter_scene(
        self,
        request: pts20201020_models.StopTestingJMeterSceneRequest,
    ) -> pts20201020_models.StopTestingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_testing_jmeter_scene_with_options(request, runtime)

    async def stop_testing_jmeter_scene_async(
        self,
        request: pts20201020_models.StopTestingJMeterSceneRequest,
    ) -> pts20201020_models.StopTestingJMeterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_testing_jmeter_scene_with_options_async(request, runtime)

    def update_pts_scene_base_line_with_options(
        self,
        tmp_req: pts20201020_models.UpdatePtsSceneBaseLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.UpdatePtsSceneBaseLineResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.UpdatePtsSceneBaseLineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.api_baselines):
            request.api_baselines_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.api_baselines, 'ApiBaselines', 'json')
        if not UtilClient.is_unset(tmp_req.scene_baseline):
            request.scene_baseline_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_baseline, 'SceneBaseline', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.UpdatePtsSceneBaseLineResponse(),
            self.do_rpcrequest('UpdatePtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_pts_scene_base_line_with_options_async(
        self,
        tmp_req: pts20201020_models.UpdatePtsSceneBaseLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pts20201020_models.UpdatePtsSceneBaseLineResponse:
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.UpdatePtsSceneBaseLineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.api_baselines):
            request.api_baselines_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.api_baselines, 'ApiBaselines', 'json')
        if not UtilClient.is_unset(tmp_req.scene_baseline):
            request.scene_baseline_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_baseline, 'SceneBaseline', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.UpdatePtsSceneBaseLineResponse(),
            await self.do_rpcrequest_async('UpdatePtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_pts_scene_base_line(
        self,
        request: pts20201020_models.UpdatePtsSceneBaseLineRequest,
    ) -> pts20201020_models.UpdatePtsSceneBaseLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_pts_scene_base_line_with_options(request, runtime)

    async def update_pts_scene_base_line_async(
        self,
        request: pts20201020_models.UpdatePtsSceneBaseLineRequest,
    ) -> pts20201020_models.UpdatePtsSceneBaseLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_pts_scene_base_line_with_options_async(request, runtime)
