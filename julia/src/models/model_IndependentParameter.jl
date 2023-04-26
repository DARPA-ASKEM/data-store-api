# This file was generated by the Julia OpenAPI Code Generator
# Do not modify this file directly. Modify the OpenAPI specification instead.


@doc raw"""IndependentParameter

    IndependentParameter(;
        id=nothing,
        model_id=nothing,
        name=nothing,
        type=nothing,
        default_value=nothing,
        state_variable=nothing,
        curie=nothing,
    )

    - id::Int64
    - model_id::Int64
    - name::String
    - type::ValueType
    - default_value::String
    - state_variable::Bool
    - curie::String
"""
Base.@kwdef mutable struct IndependentParameter <: OpenAPI.APIModel
    id::Union{Nothing, Int64} = nothing
    model_id::Union{Nothing, Int64} = nothing
    name::Union{Nothing, String} = nothing
    type = nothing # spec type: Union{ Nothing, ValueType }
    default_value::Union{Nothing, String} = nothing
    state_variable::Union{Nothing, Bool} = nothing
    curie::Union{Nothing, String} = nothing

    function IndependentParameter(id, model_id, name, type, default_value, state_variable, curie, )
        OpenAPI.validate_property(IndependentParameter, Symbol("id"), id)
        OpenAPI.validate_property(IndependentParameter, Symbol("model_id"), model_id)
        OpenAPI.validate_property(IndependentParameter, Symbol("name"), name)
        OpenAPI.validate_property(IndependentParameter, Symbol("type"), type)
        OpenAPI.validate_property(IndependentParameter, Symbol("default_value"), default_value)
        OpenAPI.validate_property(IndependentParameter, Symbol("state_variable"), state_variable)
        OpenAPI.validate_property(IndependentParameter, Symbol("curie"), curie)
        return new(id, model_id, name, type, default_value, state_variable, curie, )
    end
end # type IndependentParameter

const _property_types_IndependentParameter = Dict{Symbol,String}(Symbol("id")=>"Int64", Symbol("model_id")=>"Int64", Symbol("name")=>"String", Symbol("type")=>"ValueType", Symbol("default_value")=>"String", Symbol("state_variable")=>"Bool", Symbol("curie")=>"String", )
OpenAPI.property_type(::Type{ IndependentParameter }, name::Symbol) = Union{Nothing,eval(Base.Meta.parse(_property_types_IndependentParameter[name]))}

function check_required(o::IndependentParameter)
    o.name === nothing && (return false)
    o.type === nothing && (return false)
    o.state_variable === nothing && (return false)
    true
end

function OpenAPI.validate_property(::Type{ IndependentParameter }, name::Symbol, val)
end
