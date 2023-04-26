# This file was generated by the Julia OpenAPI Code Generator
# Do not modify this file directly. Modify the OpenAPI specification instead.

struct DatasetsApi <: OpenAPI.APIClientImpl
    client::OpenAPI.Clients.Client
end

"""
The default API base path for APIs in `DatasetsApi`.
This can be used to construct the `OpenAPI.Clients.Client` instance.
"""
basepath(::Type{ DatasetsApi }) = "http://localhost"

const _returntypes_create_dataset_datasets_post_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_create_dataset_datasets_post(_api::DatasetsApi, dataset::Dataset; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "POST", _returntypes_create_dataset_datasets_post_DatasetsApi, "/datasets", [], dataset)
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["application/json", ] : [_mediaType])
    return _ctx
end

@doc raw"""Create Dataset

Create a dataset

Params:
- dataset::Dataset (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function create_dataset_datasets_post(_api::DatasetsApi, dataset::Dataset; _mediaType=nothing)
    _ctx = _oacinternal_create_dataset_datasets_post(_api, dataset; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function create_dataset_datasets_post(_api::DatasetsApi, response_stream::Channel, dataset::Dataset; _mediaType=nothing)
    _ctx = _oacinternal_create_dataset_datasets_post(_api, dataset; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_create_feature_datasets_features_post_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_create_feature_datasets_features_post(_api::DatasetsApi, feature::Feature; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "POST", _returntypes_create_feature_datasets_features_post_DatasetsApi, "/datasets/features", [], feature)
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["application/json", ] : [_mediaType])
    return _ctx
end

@doc raw"""Create Feature

Create a feature

Params:
- feature::Feature (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function create_feature_datasets_features_post(_api::DatasetsApi, feature::Feature; _mediaType=nothing)
    _ctx = _oacinternal_create_feature_datasets_features_post(_api, feature; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function create_feature_datasets_features_post(_api::DatasetsApi, response_stream::Channel, feature::Feature; _mediaType=nothing)
    _ctx = _oacinternal_create_feature_datasets_features_post(_api, feature; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_create_qualifier_datasets_qualifiers_post_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_create_qualifier_datasets_qualifiers_post(_api::DatasetsApi, body_create_qualifier_datasets_qualifiers_post::BodyCreateQualifierDatasetsQualifiersPost; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "POST", _returntypes_create_qualifier_datasets_qualifiers_post_DatasetsApi, "/datasets/qualifiers", [], body_create_qualifier_datasets_qualifiers_post)
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["application/json", ] : [_mediaType])
    return _ctx
end

@doc raw"""Create Qualifier

Create a qualifier

Params:
- body_create_qualifier_datasets_qualifiers_post::BodyCreateQualifierDatasetsQualifiersPost (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function create_qualifier_datasets_qualifiers_post(_api::DatasetsApi, body_create_qualifier_datasets_qualifiers_post::BodyCreateQualifierDatasetsQualifiersPost; _mediaType=nothing)
    _ctx = _oacinternal_create_qualifier_datasets_qualifiers_post(_api, body_create_qualifier_datasets_qualifiers_post; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function create_qualifier_datasets_qualifiers_post(_api::DatasetsApi, response_stream::Channel, body_create_qualifier_datasets_qualifiers_post::BodyCreateQualifierDatasetsQualifiersPost; _mediaType=nothing)
    _ctx = _oacinternal_create_qualifier_datasets_qualifiers_post(_api, body_create_qualifier_datasets_qualifiers_post; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_delete_dataset_datasets_id_delete_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_delete_dataset_datasets_id_delete(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "DELETE", _returntypes_delete_dataset_datasets_id_delete_DatasetsApi, "/datasets/{id}", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Delete Dataset

Delete a dataset by ID

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function delete_dataset_datasets_id_delete(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_delete_dataset_datasets_id_delete(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function delete_dataset_datasets_id_delete(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_delete_dataset_datasets_id_delete(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_delete_feature_datasets_features_id_delete_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_delete_feature_datasets_features_id_delete(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "DELETE", _returntypes_delete_feature_datasets_features_id_delete_DatasetsApi, "/datasets/features/{id}", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Delete Feature

Delete a feature by ID

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function delete_feature_datasets_features_id_delete(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_delete_feature_datasets_features_id_delete(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function delete_feature_datasets_features_id_delete(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_delete_feature_datasets_features_id_delete(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_delete_qualifier_datasets_qualifiers_id_delete_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_delete_qualifier_datasets_qualifiers_id_delete(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "DELETE", _returntypes_delete_qualifier_datasets_qualifiers_id_delete_DatasetsApi, "/datasets/qualifiers/{id}", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Delete Qualifier

Delete a qualifier by ID

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function delete_qualifier_datasets_qualifiers_id_delete(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_delete_qualifier_datasets_qualifiers_id_delete(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function delete_qualifier_datasets_qualifiers_id_delete(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_delete_qualifier_datasets_qualifiers_id_delete(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_deprecate_dataset_datasets_deprecate_id_post_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_deprecate_dataset_datasets_deprecate_id_post(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "POST", _returntypes_deprecate_dataset_datasets_deprecate_id_post_DatasetsApi, "/datasets/deprecate/{id}", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Deprecate Dataset

Toggle a dataset's deprecated status by ID

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function deprecate_dataset_datasets_deprecate_id_post(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_deprecate_dataset_datasets_deprecate_id_post(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function deprecate_dataset_datasets_deprecate_id_post(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_deprecate_dataset_datasets_deprecate_id_post(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_csv_from_dataset_datasets_id_file_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_csv_from_dataset_datasets_id_file_get(_api::DatasetsApi, id::Int64; wide_format=nothing, row_limit=nothing, _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_csv_from_dataset_datasets_id_file_get_DatasetsApi, "/datasets/{id}/file", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "wide_format", wide_format)  # type Bool
    OpenAPI.Clients.set_param(_ctx.query, "row_limit", row_limit)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Csv From Dataset

Gets the csv of an annotated dataset that is registered via the data-annotation tool.

Params:
- id::Int64 (required)
- wide_format::Bool
- row_limit::Int64

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_csv_from_dataset_datasets_id_file_get(_api::DatasetsApi, id::Int64; wide_format=nothing, row_limit=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_csv_from_dataset_datasets_id_file_get(_api, id; wide_format=wide_format, row_limit=row_limit, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_csv_from_dataset_datasets_id_file_get(_api::DatasetsApi, response_stream::Channel, id::Int64; wide_format=nothing, row_limit=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_csv_from_dataset_datasets_id_file_get(_api, id; wide_format=wide_format, row_limit=row_limit, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_csv_from_dataset_depr_datasets_id_download_rawfile_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_csv_from_dataset_depr_datasets_id_download_rawfile_get(_api::DatasetsApi, id::Int64; wide_format=nothing, row_limit=nothing, _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_csv_from_dataset_depr_datasets_id_download_rawfile_get_DatasetsApi, "/datasets/{id}/download/rawfile", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "wide_format", wide_format)  # type Bool
    OpenAPI.Clients.set_param(_ctx.query, "row_limit", row_limit)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Csv From Dataset Depr

Gets the csv of an annotated dataset that is registered via the data-annotation tool.

Params:
- id::Int64 (required)
- wide_format::Bool
- row_limit::Int64

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_csv_from_dataset_depr_datasets_id_download_rawfile_get(_api::DatasetsApi, id::Int64; wide_format=nothing, row_limit=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_csv_from_dataset_depr_datasets_id_download_rawfile_get(_api, id; wide_format=wide_format, row_limit=row_limit, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_csv_from_dataset_depr_datasets_id_download_rawfile_get(_api::DatasetsApi, response_stream::Channel, id::Int64; wide_format=nothing, row_limit=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_csv_from_dataset_depr_datasets_id_download_rawfile_get(_api, id; wide_format=wide_format, row_limit=row_limit, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_dataset_datasets_id_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_dataset_datasets_id_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_dataset_datasets_id_get_DatasetsApi, "/datasets/{id}", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Dataset

Get a specific dataset by ID

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_dataset_datasets_id_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_get_dataset_datasets_id_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_dataset_datasets_id_get(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_get_dataset_datasets_id_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_datasets_datasets_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_datasets_datasets_get(_api::DatasetsApi; page_size=nothing, page=nothing, is_sim_run=nothing, _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_datasets_datasets_get_DatasetsApi, "/datasets", [])
    OpenAPI.Clients.set_param(_ctx.query, "page_size", page_size)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "page", page)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "is_sim_run", is_sim_run)  # type Bool
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Datasets

Get a specific number of datasets

Params:
- page_size::Int64
- page::Int64
- is_sim_run::Bool

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_datasets_datasets_get(_api::DatasetsApi; page_size=nothing, page=nothing, is_sim_run=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_datasets_datasets_get(_api; page_size=page_size, page=page, is_sim_run=is_sim_run, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_datasets_datasets_get(_api::DatasetsApi, response_stream::Channel; page_size=nothing, page=nothing, is_sim_run=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_datasets_datasets_get(_api; page_size=page_size, page=page, is_sim_run=is_sim_run, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_feature_datasets_features_id_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_feature_datasets_features_id_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_feature_datasets_features_id_get_DatasetsApi, "/datasets/features/{id}", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Feature

Get a specific feature by ID

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_feature_datasets_features_id_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_get_feature_datasets_features_id_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_feature_datasets_features_id_get(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_get_feature_datasets_features_id_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_features_datasets_features_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_features_datasets_features_get(_api::DatasetsApi; page_size=nothing, page=nothing, _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_features_datasets_features_get_DatasetsApi, "/datasets/features", [])
    OpenAPI.Clients.set_param(_ctx.query, "page_size", page_size)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "page", page)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Features

Get a specified number of features

Params:
- page_size::Int64
- page::Int64

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_features_datasets_features_get(_api::DatasetsApi; page_size=nothing, page=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_features_datasets_features_get(_api; page_size=page_size, page=page, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_features_datasets_features_get(_api::DatasetsApi, response_stream::Channel; page_size=nothing, page=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_features_datasets_features_get(_api; page_size=page_size, page=page, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_qualifier_datasets_qualifiers_id_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_qualifier_datasets_qualifiers_id_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_qualifier_datasets_qualifiers_id_get_DatasetsApi, "/datasets/qualifiers/{id}", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Qualifier

Get a specific qualifier by ID

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_qualifier_datasets_qualifiers_id_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_get_qualifier_datasets_qualifiers_id_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_qualifier_datasets_qualifiers_id_get(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_get_qualifier_datasets_qualifiers_id_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_get_qualifiers_datasets_qualifiers_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_get_qualifiers_datasets_qualifiers_get(_api::DatasetsApi; page_size=nothing, page=nothing, _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_get_qualifiers_datasets_qualifiers_get_DatasetsApi, "/datasets/qualifiers", [])
    OpenAPI.Clients.set_param(_ctx.query, "page_size", page_size)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "page", page)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Get Qualifiers

Get a specific number of qualifiers

Params:
- page_size::Int64
- page::Int64

Return: Any, OpenAPI.Clients.ApiResponse
"""
function get_qualifiers_datasets_qualifiers_get(_api::DatasetsApi; page_size=nothing, page=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_qualifiers_datasets_qualifiers_get(_api; page_size=page_size, page=page, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function get_qualifiers_datasets_qualifiers_get(_api::DatasetsApi, response_stream::Channel; page_size=nothing, page=nothing, _mediaType=nothing)
    _ctx = _oacinternal_get_qualifiers_datasets_qualifiers_get(_api; page_size=page_size, page=page, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_search_feature_datasets_id_features_get_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_search_feature_datasets_id_features_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "GET", _returntypes_search_feature_datasets_id_features_get_DatasetsApi, "/datasets/{id}/features", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? [] : [_mediaType])
    return _ctx
end

@doc raw"""Search Feature

Search features by dataset id and/or name

Params:
- id::Int64 (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function search_feature_datasets_id_features_get(_api::DatasetsApi, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_search_feature_datasets_id_features_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function search_feature_datasets_id_features_get(_api::DatasetsApi, response_stream::Channel, id::Int64; _mediaType=nothing)
    _ctx = _oacinternal_search_feature_datasets_id_features_get(_api, id; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_update_dataset_datasets_id_patch_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_update_dataset_datasets_id_patch(_api::DatasetsApi, id::Int64, dataset::Dataset; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "PATCH", _returntypes_update_dataset_datasets_id_patch_DatasetsApi, "/datasets/{id}", [], dataset)
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["application/json", ] : [_mediaType])
    return _ctx
end

@doc raw"""Update Dataset

Update a dataset by ID

Params:
- id::Int64 (required)
- dataset::Dataset (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function update_dataset_datasets_id_patch(_api::DatasetsApi, id::Int64, dataset::Dataset; _mediaType=nothing)
    _ctx = _oacinternal_update_dataset_datasets_id_patch(_api, id, dataset; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function update_dataset_datasets_id_patch(_api::DatasetsApi, response_stream::Channel, id::Int64, dataset::Dataset; _mediaType=nothing)
    _ctx = _oacinternal_update_dataset_datasets_id_patch(_api, id, dataset; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_update_feature_datasets_features_id_patch_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_update_feature_datasets_features_id_patch(_api::DatasetsApi, id::Int64, feature::Feature; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "PATCH", _returntypes_update_feature_datasets_features_id_patch_DatasetsApi, "/datasets/features/{id}", [], feature)
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["application/json", ] : [_mediaType])
    return _ctx
end

@doc raw"""Update Feature

Update a feature by ID

Params:
- id::Int64 (required)
- feature::Feature (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function update_feature_datasets_features_id_patch(_api::DatasetsApi, id::Int64, feature::Feature; _mediaType=nothing)
    _ctx = _oacinternal_update_feature_datasets_features_id_patch(_api, id, feature; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function update_feature_datasets_features_id_patch(_api::DatasetsApi, response_stream::Channel, id::Int64, feature::Feature; _mediaType=nothing)
    _ctx = _oacinternal_update_feature_datasets_features_id_patch(_api, id, feature; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_update_qualifier_datasets_qualifiers_id_patch_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_update_qualifier_datasets_qualifiers_id_patch(_api::DatasetsApi, id::Int64, qualifier::Qualifier; _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "PATCH", _returntypes_update_qualifier_datasets_qualifiers_id_patch_DatasetsApi, "/datasets/qualifiers/{id}", [], qualifier)
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["application/json", ] : [_mediaType])
    return _ctx
end

@doc raw"""Update Qualifier

Update a qualifier by ID

Params:
- id::Int64 (required)
- qualifier::Qualifier (required)

Return: Any, OpenAPI.Clients.ApiResponse
"""
function update_qualifier_datasets_qualifiers_id_patch(_api::DatasetsApi, id::Int64, qualifier::Qualifier; _mediaType=nothing)
    _ctx = _oacinternal_update_qualifier_datasets_qualifiers_id_patch(_api, id, qualifier; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function update_qualifier_datasets_qualifiers_id_patch(_api::DatasetsApi, response_stream::Channel, id::Int64, qualifier::Qualifier; _mediaType=nothing)
    _ctx = _oacinternal_update_qualifier_datasets_qualifiers_id_patch(_api, id, qualifier; _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_upload_file_datasets_id_file_post_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_upload_file_datasets_id_file_post(_api::DatasetsApi, id::Int64, file::String; filename=nothing, _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "POST", _returntypes_upload_file_datasets_id_file_post_DatasetsApi, "/datasets/{id}/file", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "filename", filename)  # type String
    OpenAPI.Clients.set_param(_ctx.file, "file", file)  # type String
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["multipart/form-data", ] : [_mediaType])
    return _ctx
end

@doc raw"""Upload File

Upload a file to the DATASET_BASE_STORAGE_URL  Args:     id (int): Dataset ID.     file (UploadFile, optional): Upload of file-like object.     filename (Optional[str], optional): Allows the specification of     a particular filename at upload. Defaults to None.  Returns:     Reponse: FastAPI Response object containing     information about the uploaded file.

Params:
- id::Int64 (required)
- file::String (required)
- filename::String

Return: Any, OpenAPI.Clients.ApiResponse
"""
function upload_file_datasets_id_file_post(_api::DatasetsApi, id::Int64, file::String; filename=nothing, _mediaType=nothing)
    _ctx = _oacinternal_upload_file_datasets_id_file_post(_api, id, file; filename=filename, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function upload_file_datasets_id_file_post(_api::DatasetsApi, response_stream::Channel, id::Int64, file::String; filename=nothing, _mediaType=nothing)
    _ctx = _oacinternal_upload_file_datasets_id_file_post(_api, id, file; filename=filename, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

const _returntypes_upload_file_depr_datasets_id_upload_file_post_DatasetsApi = Dict{Regex,Type}(
    Regex("^" * replace("200", "x"=>".") * "\$") => Any,
    Regex("^" * replace("422", "x"=>".") * "\$") => HTTPValidationError,
)

function _oacinternal_upload_file_depr_datasets_id_upload_file_post(_api::DatasetsApi, id::Int64, file::String; filename=nothing, _mediaType=nothing)
    _ctx = OpenAPI.Clients.Ctx(_api.client, "POST", _returntypes_upload_file_depr_datasets_id_upload_file_post_DatasetsApi, "/datasets/{id}/upload/file", [])
    OpenAPI.Clients.set_param(_ctx.path, "id", id)  # type Int64
    OpenAPI.Clients.set_param(_ctx.query, "filename", filename)  # type String
    OpenAPI.Clients.set_param(_ctx.file, "file", file)  # type String
    OpenAPI.Clients.set_header_accept(_ctx, ["application/json", ])
    OpenAPI.Clients.set_header_content_type(_ctx, (_mediaType === nothing) ? ["multipart/form-data", ] : [_mediaType])
    return _ctx
end

@doc raw"""Upload File Depr

Upload a file to the DATASET_BASE_STORAGE_URL  Args:     id (int): Dataset ID.     file (UploadFile, optional): Upload of file-like object.     filename (Optional[str], optional): Allows the specification of     a particular filename at upload. Defaults to None.  Returns:     Reponse: FastAPI Response object containing     information about the uploaded file.

Params:
- id::Int64 (required)
- file::String (required)
- filename::String

Return: Any, OpenAPI.Clients.ApiResponse
"""
function upload_file_depr_datasets_id_upload_file_post(_api::DatasetsApi, id::Int64, file::String; filename=nothing, _mediaType=nothing)
    _ctx = _oacinternal_upload_file_depr_datasets_id_upload_file_post(_api, id, file; filename=filename, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx)
end

function upload_file_depr_datasets_id_upload_file_post(_api::DatasetsApi, response_stream::Channel, id::Int64, file::String; filename=nothing, _mediaType=nothing)
    _ctx = _oacinternal_upload_file_depr_datasets_id_upload_file_post(_api, id, file; filename=filename, _mediaType=_mediaType)
    return OpenAPI.Clients.exec(_ctx, response_stream)
end

export create_dataset_datasets_post
export create_feature_datasets_features_post
export create_qualifier_datasets_qualifiers_post
export delete_dataset_datasets_id_delete
export delete_feature_datasets_features_id_delete
export delete_qualifier_datasets_qualifiers_id_delete
export deprecate_dataset_datasets_deprecate_id_post
export get_csv_from_dataset_datasets_id_file_get
export get_csv_from_dataset_depr_datasets_id_download_rawfile_get
export get_dataset_datasets_id_get
export get_datasets_datasets_get
export get_feature_datasets_features_id_get
export get_features_datasets_features_get
export get_qualifier_datasets_qualifiers_id_get
export get_qualifiers_datasets_qualifiers_get
export search_feature_datasets_id_features_get
export update_dataset_datasets_id_patch
export update_feature_datasets_features_id_patch
export update_qualifier_datasets_qualifiers_id_patch
export upload_file_datasets_id_file_post
export upload_file_depr_datasets_id_upload_file_post
