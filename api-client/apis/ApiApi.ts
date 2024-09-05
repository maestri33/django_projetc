/* tslint:disable */
/* eslint-disable */
/**
 * maestri-mvp
 * Juntos dia após dia crescemos dentro de um propósito. Acreditamos que a educação é o maior instrumento que Deus usa para mudar o mundo.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import type {
  CustomUser,
  JWT,
  Login,
  LoginResponse,
  OtpRequest,
  PasswordChange,
  PatchedCustomUser,
  Register,
  RestAuthDetail,
  TokenRefresh,
  TokenVerify,
} from '../models/index';
import {
    CustomUserFromJSON,
    CustomUserToJSON,
    JWTFromJSON,
    JWTToJSON,
    LoginFromJSON,
    LoginToJSON,
    LoginResponseFromJSON,
    LoginResponseToJSON,
    OtpRequestFromJSON,
    OtpRequestToJSON,
    PasswordChangeFromJSON,
    PasswordChangeToJSON,
    PatchedCustomUserFromJSON,
    PatchedCustomUserToJSON,
    RegisterFromJSON,
    RegisterToJSON,
    RestAuthDetailFromJSON,
    RestAuthDetailToJSON,
    TokenRefreshFromJSON,
    TokenRefreshToJSON,
    TokenVerifyFromJSON,
    TokenVerifyToJSON,
} from '../models/index';

export interface ApiAuthLoginCreateRequest {
    login: Login;
}

export interface ApiAuthPasswordChangeCreateRequest {
    passwordChange: PasswordChange;
}

export interface ApiAuthRegisterCreateRequest {
    register: Register;
}

export interface ApiAuthTokenRefreshCreateRequest {
    tokenRefresh: Omit<TokenRefresh, 'access'>;
}

export interface ApiAuthTokenVerifyCreateRequest {
    tokenVerify: TokenVerify;
}

export interface ApiAuthUserPartialUpdateRequest {
    patchedCustomUser?: Omit<PatchedCustomUser, 'id'|'avatar_url'|'get_display_name'>;
}

export interface ApiAuthUserUpdateRequest {
    customUser?: Omit<CustomUser, 'id'|'avatar_url'|'get_display_name'>;
}

export interface ApiAuthVerifyOtpCreateRequest {
    otpRequest: OtpRequest;
}

/**
 * 
 */
export class ApiApi extends runtime.BaseAPI {

    /**
     * Custom login view that checks if 2FA is enabled for the user.
     */
    async apiAuthLoginCreateRaw(requestParameters: ApiAuthLoginCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<LoginResponse>> {
        if (requestParameters['login'] == null) {
            throw new runtime.RequiredError(
                'login',
                'Required parameter "login" was null or undefined when calling apiAuthLoginCreate().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/login/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: LoginToJSON(requestParameters['login']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => LoginResponseFromJSON(jsonValue));
    }

    /**
     * Custom login view that checks if 2FA is enabled for the user.
     */
    async apiAuthLoginCreate(requestParameters: ApiAuthLoginCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<LoginResponse> {
        const response = await this.apiAuthLoginCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Calls Django logout method and delete the Token object assigned to the current User object.  Accepts/Returns nothing.
     */
    async apiAuthLogoutCreateRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<RestAuthDetail>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/logout/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => RestAuthDetailFromJSON(jsonValue));
    }

    /**
     * Calls Django logout method and delete the Token object assigned to the current User object.  Accepts/Returns nothing.
     */
    async apiAuthLogoutCreate(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<RestAuthDetail> {
        const response = await this.apiAuthLogoutCreateRaw(initOverrides);
        return await response.value();
    }

    /**
     * Calls Django logout method and delete the Token object assigned to the current User object.  Accepts/Returns nothing.
     */
    async apiAuthLogoutRetrieveRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<RestAuthDetail>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/logout/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => RestAuthDetailFromJSON(jsonValue));
    }

    /**
     * Calls Django logout method and delete the Token object assigned to the current User object.  Accepts/Returns nothing.
     */
    async apiAuthLogoutRetrieve(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<RestAuthDetail> {
        const response = await this.apiAuthLogoutRetrieveRaw(initOverrides);
        return await response.value();
    }

    /**
     * Calls Django Auth SetPasswordForm save method.  Accepts the following POST parameters: new_password1, new_password2 Returns the success/fail message.
     */
    async apiAuthPasswordChangeCreateRaw(requestParameters: ApiAuthPasswordChangeCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<RestAuthDetail>> {
        if (requestParameters['passwordChange'] == null) {
            throw new runtime.RequiredError(
                'passwordChange',
                'Required parameter "passwordChange" was null or undefined when calling apiAuthPasswordChangeCreate().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/password/change/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: PasswordChangeToJSON(requestParameters['passwordChange']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => RestAuthDetailFromJSON(jsonValue));
    }

    /**
     * Calls Django Auth SetPasswordForm save method.  Accepts the following POST parameters: new_password1, new_password2 Returns the success/fail message.
     */
    async apiAuthPasswordChangeCreate(requestParameters: ApiAuthPasswordChangeCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<RestAuthDetail> {
        const response = await this.apiAuthPasswordChangeCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async apiAuthRegisterCreateRaw(requestParameters: ApiAuthRegisterCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<JWT>> {
        if (requestParameters['register'] == null) {
            throw new runtime.RequiredError(
                'register',
                'Required parameter "register" was null or undefined when calling apiAuthRegisterCreate().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/register/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: RegisterToJSON(requestParameters['register']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => JWTFromJSON(jsonValue));
    }

    /**
     */
    async apiAuthRegisterCreate(requestParameters: ApiAuthRegisterCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<JWT> {
        const response = await this.apiAuthRegisterCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
     */
    async apiAuthTokenRefreshCreateRaw(requestParameters: ApiAuthTokenRefreshCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<TokenRefresh>> {
        if (requestParameters['tokenRefresh'] == null) {
            throw new runtime.RequiredError(
                'tokenRefresh',
                'Required parameter "tokenRefresh" was null or undefined when calling apiAuthTokenRefreshCreate().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/api/auth/token/refresh/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: TokenRefreshToJSON(requestParameters['tokenRefresh']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => TokenRefreshFromJSON(jsonValue));
    }

    /**
     * Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
     */
    async apiAuthTokenRefreshCreate(requestParameters: ApiAuthTokenRefreshCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<TokenRefresh> {
        const response = await this.apiAuthTokenRefreshCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Takes a token and indicates if it is valid.  This view provides no information about a token\'s fitness for a particular use.
     */
    async apiAuthTokenVerifyCreateRaw(requestParameters: ApiAuthTokenVerifyCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<TokenVerify>> {
        if (requestParameters['tokenVerify'] == null) {
            throw new runtime.RequiredError(
                'tokenVerify',
                'Required parameter "tokenVerify" was null or undefined when calling apiAuthTokenVerifyCreate().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/api/auth/token/verify/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: TokenVerifyToJSON(requestParameters['tokenVerify']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => TokenVerifyFromJSON(jsonValue));
    }

    /**
     * Takes a token and indicates if it is valid.  This view provides no information about a token\'s fitness for a particular use.
     */
    async apiAuthTokenVerifyCreate(requestParameters: ApiAuthTokenVerifyCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<TokenVerify> {
        const response = await this.apiAuthTokenVerifyCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.
     */
    async apiAuthUserPartialUpdateRaw(requestParameters: ApiAuthUserPartialUpdateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<CustomUser>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/user/`,
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: PatchedCustomUserToJSON(requestParameters['patchedCustomUser']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => CustomUserFromJSON(jsonValue));
    }

    /**
     * Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.
     */
    async apiAuthUserPartialUpdate(requestParameters: ApiAuthUserPartialUpdateRequest = {}, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<CustomUser> {
        const response = await this.apiAuthUserPartialUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.
     */
    async apiAuthUserRetrieveRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<CustomUser>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/user/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => CustomUserFromJSON(jsonValue));
    }

    /**
     * Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.
     */
    async apiAuthUserRetrieve(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<CustomUser> {
        const response = await this.apiAuthUserRetrieveRaw(initOverrides);
        return await response.value();
    }

    /**
     * Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.
     */
    async apiAuthUserUpdateRaw(requestParameters: ApiAuthUserUpdateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<CustomUser>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/user/`,
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: CustomUserToJSON(requestParameters['customUser']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => CustomUserFromJSON(jsonValue));
    }

    /**
     * Reads and updates UserModel fields Accepts GET, PUT, PATCH methods.  Default accepted fields: username, first_name, last_name Default display fields: pk, username, email, first_name, last_name Read-only fields: pk, email  Returns UserModel fields.
     */
    async apiAuthUserUpdate(requestParameters: ApiAuthUserUpdateRequest = {}, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<CustomUser> {
        const response = await this.apiAuthUserUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async apiAuthVerifyOtpCreateRaw(requestParameters: ApiAuthVerifyOtpCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<JWT>> {
        if (requestParameters['otpRequest'] == null) {
            throw new runtime.RequiredError(
                'otpRequest',
                'Required parameter "otpRequest" was null or undefined when calling apiAuthVerifyOtpCreate().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        if (this.configuration && this.configuration.accessToken) {
            const token = this.configuration.accessToken;
            const tokenString = await token("jwtAuth", []);

            if (tokenString) {
                headerParameters["Authorization"] = `Bearer ${tokenString}`;
            }
        }
        const response = await this.request({
            path: `/api/auth/verify-otp/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: OtpRequestToJSON(requestParameters['otpRequest']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => JWTFromJSON(jsonValue));
    }

    /**
     */
    async apiAuthVerifyOtpCreate(requestParameters: ApiAuthVerifyOtpCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<JWT> {
        const response = await this.apiAuthVerifyOtpCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
