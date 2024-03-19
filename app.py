from flask import Flask, render_template,  jsonify,request
import requests


app = Flask(__name__)
# 예시 데이터



token_info = {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNpZ25pbmdfMiJ9.eyJzdWIiOiJ2bXdhcmVpZDo4ZWM0NDQ3NC0zZmQxLTQ2YmItYmYwZS03MzRhMzkyOTUyYWUiLCJpc3MiOiJodHRwczovL2dhei5jc3AtdmlkbS1wcm9kLmNvbSIsImNvbnRleHRfbmFtZSI6ImE2ODQxODVhLTM3YjQtNDdkZS04NGI0LTRmY2M0Zjc3NjAwZCIsImF6cCI6ImNzcF9wcmRfZ2F6X2ludGVybmFsX2NsaWVudF9pZCIsImF1dGhvcml6YXRpb25fZGV0YWlscyI6W10sImRvbWFpbiI6InZtd2FyZWlkIiwiY29udGV4dCI6IjliYjRhZjI1LTljMWYtNDJhZS1iYTQ2LTVmODY4ZGI2OWJkYyIsInBlcm1zIjpbImV4dGVybmFsLzY3ZTU5ZDBjLTBiMjAtNDczYi04YzRkLTU1OTUyODM2NjRkOS92bWNmczpjb25zb2xlLWFkbWluIiwiY3NwOm9yZ19tZW1iZXIiLCJjc3A6c29mdHdhcmVfaW5zdGFsbGVyIiwiZXh0ZXJuYWwvMGU0NTUyMzctMWQzYS00ZTAzLWIyMzEtZjI5ZjU3ZWFhZGUyL3ZjZHI6Y29uc29sZS1hZG1pbiIsImV4dGVybmFsL3liVWRvVEMwNWtZRkM5Wkc1NjBrcHNuMEk4TV8vbnN4OmNsb3VkX2FkbWluIiwiZXh0ZXJuYWwvMDc5YjY5ODItZTM0Ni00ZjFmLWE5MTctZDg4ZDIzZDQ4NTAzL3NlcnZpY2U6YWRtaW4iLCJleHRlcm5hbC95YlVkb1RDMDVrWUZDOVpHNTYwa3BzbjBJOE1fL3ZtYy11c2VyOmZ1bGwiLCJleHRlcm5hbC95YlVkb1RDMDVrWUZDOVpHNTYwa3BzbjBJOE1fL25zeDpuZXR3b3JrX29wIiwiY3NwOm9yZ19vd25lciIsImV4dGVybmFsL3liVWRvVEMwNWtZRkM5Wkc1NjBrcHNuMEk4TV8vbnN4Om5ldHdvcmtfZW5naW5lZXIiLCJleHRlcm5hbC8wZTQ1NTIzNy0xZDNhLTRlMDMtYjIzMS1mMjlmNTdlYWFkZTIvdmNkcjphZG1pbmlzdHJhdG9yIiwiZXh0ZXJuYWwveWJVZG9UQzA1a1lGQzlaRzU2MGtwc24wSThNXy9uc3g6c2VjdXJpdHlfZW5naW5lZXIiLCJleHRlcm5hbC8wNzliNjk4Mi1lMzQ2LTRmMWYtYTkxNy1kODhkMjNkNDg1MDMvc2VydmljZTptZW1iZXIiLCJleHRlcm5hbC83Y0oybmdTX2hSQ1lfYkliV3VjTTRLV1F3T29fL3Zybi9vcmc6YTY4NDE4NWEtMzdiNC00N2RlLTg0YjQtNGZjYzRmNzc2MDBkL2luc3RhbmNlOjc2YWNkMGI3LTQ2OWMtNGZmOC1iODdiLTg2NDliOGM2NDViNi9sb2ctaW50ZWxsaWdlbmNlOmFkbWluIiwiZXh0ZXJuYWwvN2NKMm5nU19oUkNZX2JJYld1Y000S1dRd09vXy9sb2ctaW50ZWxsaWdlbmNlOmFkbWluIiwiZXh0ZXJuYWwvNjdlNTlkMGMtMGIyMC00NzNiLThjNGQtNTU5NTI4MzY2NGQ5L3ZtY2ZzOmFkbWluaXN0cmF0b3IiLCJleHRlcm5hbC80NTExMjFjOC00NjM4LTRjNzMtYjFjYi00MWExZjE5ZDAyN2Evc3J2LW1hcmtldHBsYWNlOm1hcmtldHBsYWNldXNlciIsImV4dGVybmFsL3liVWRvVEMwNWtZRkM5Wkc1NjBrcHNuMEk4TV8vbnN4OnNlY3VyaXR5X29wIl0sImV4cCI6MTcxMDgzMDk0MywiaWF0IjoxNzEwODI5MTQzLCJqdGkiOiIyMzY5NzI3My0zNmFkLTRlZGMtODdhYy01OTZmMWE0MzU3ZWUiLCJhY2N0Ijoia29vQG1lZ2F6b25lLmNvbSIsInVzZXJuYW1lIjoia29vQG1lZ2F6b25lLmNvbSJ9.hkWJUeIeJMKWylUQNt6Xfo5twwzI5H3YMa5EOV27eri95Ff0jJ2u0pW7q3N-m0pEty6ZLv0fQxzshWVqQlmPY8q60mfm2AJqzKobROj8_Up_FFA07dmAPfFeJvwZ5fiSS1nKGr7hIrwZe4AYjFF9Uyi-_Fntcg5Ja5NDF-v8gPOrUTzejV_NZ6k1tQNcWa66NLI44RyLgMbTyMfJUQxVlJaeDXvfiTKqwpbmMr2ZezgPGZ-1xFsmf6Te6WTVR048CvpAkntkZxteN8m6w2m_0sYRIvl890rMCJmXULqAKpmOlhHMJ9N5MGv1t-qDAUlZPO5YkfDvAUzLMdlQ92Kqzg",
  
    "refresh_token": "a7Z3Iqj62ZLivYgk9CeFq4PilzGWdgZ6jCAOi6fBeaJTYsHneayEad0v1aQBqRj8"
}

csp_auth_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNpZ25pbmdfMiJ9.eyJzdWIiOiJ2bXdhcmVpZDo4ZWM0NDQ3NC0zZmQxLTQ2YmItYmYwZS03MzRhMzkyOTUyYWUiLCJpc3MiOiJodHRwczovL2dhei5jc3AtdmlkbS1wcm9kLmNvbSIsImNvbnRleHRfbmFtZSI6ImE2ODQxODVhLTM3YjQtNDdkZS04NGI0LTRmY2M0Zjc3NjAwZCIsImF6cCI6ImNzcF9wcmRfZ2F6X2ludGVybmFsX2NsaWVudF9pZCIsImF1dGhvcml6YXRpb25fZGV0YWlscyI6W10sImRvbWFpbiI6InZtd2FyZWlkIiwiY29udGV4dCI6IjliYjRhZjI1LTljMWYtNDJhZS1iYTQ2LTVmODY4ZGI2OWJkYyIsInBlcm1zIjpbImV4dGVybmFsLzY3ZTU5ZDBjLTBiMjAtNDczYi04YzRkLTU1OTUyODM2NjRkOS92bWNmczpjb25zb2xlLWFkbWluIiwiY3NwOm9yZ19tZW1iZXIiLCJjc3A6c29mdHdhcmVfaW5zdGFsbGVyIiwiZXh0ZXJuYWwvMGU0NTUyMzctMWQzYS00ZTAzLWIyMzEtZjI5ZjU3ZWFhZGUyL3ZjZHI6Y29uc29sZS1hZG1pbiIsImV4dGVybmFsL3liVWRvVEMwNWtZRkM5Wkc1NjBrcHNuMEk4TV8vbnN4OmNsb3VkX2FkbWluIiwiZXh0ZXJuYWwvMDc5YjY5ODItZTM0Ni00ZjFmLWE5MTctZDg4ZDIzZDQ4NTAzL3NlcnZpY2U6YWRtaW4iLCJleHRlcm5hbC95YlVkb1RDMDVrWUZDOVpHNTYwa3BzbjBJOE1fL3ZtYy11c2VyOmZ1bGwiLCJleHRlcm5hbC95YlVkb1RDMDVrWUZDOVpHNTYwa3BzbjBJOE1fL25zeDpuZXR3b3JrX29wIiwiY3NwOm9yZ19vd25lciIsImV4dGVybmFsL3liVWRvVEMwNWtZRkM5Wkc1NjBrcHNuMEk4TV8vbnN4Om5ldHdvcmtfZW5naW5lZXIiLCJleHRlcm5hbC8wZTQ1NTIzNy0xZDNhLTRlMDMtYjIzMS1mMjlmNTdlYWFkZTIvdmNkcjphZG1pbmlzdHJhdG9yIiwiZXh0ZXJuYWwveWJVZG9UQzA1a1lGQzlaRzU2MGtwc24wSThNXy9uc3g6c2VjdXJpdHlfZW5naW5lZXIiLCJleHRlcm5hbC8wNzliNjk4Mi1lMzQ2LTRmMWYtYTkxNy1kODhkMjNkNDg1MDMvc2VydmljZTptZW1iZXIiLCJleHRlcm5hbC83Y0oybmdTX2hSQ1lfYkliV3VjTTRLV1F3T29fL3Zybi9vcmc6YTY4NDE4NWEtMzdiNC00N2RlLTg0YjQtNGZjYzRmNzc2MDBkL2luc3RhbmNlOjc2YWNkMGI3LTQ2OWMtNGZmOC1iODdiLTg2NDliOGM2NDViNi9sb2ctaW50ZWxsaWdlbmNlOmFkbWluIiwiZXh0ZXJuYWwvN2NKMm5nU19oUkNZX2JJYld1Y000S1dRd09vXy9sb2ctaW50ZWxsaWdlbmNlOmFkbWluIiwiZXh0ZXJuYWwvNjdlNTlkMGMtMGIyMC00NzNiLThjNGQtNTU5NTI4MzY2NGQ5L3ZtY2ZzOmFkbWluaXN0cmF0b3IiLCJleHRlcm5hbC80NTExMjFjOC00NjM4LTRjNzMtYjFjYi00MWExZjE5ZDAyN2Evc3J2LW1hcmtldHBsYWNlOm1hcmtldHBsYWNldXNlciIsImV4dGVybmFsL3liVWRvVEMwNWtZRkM5Wkc1NjBrcHNuMEk4TV8vbnN4OnNlY3VyaXR5X29wIl0sImV4cCI6MTcxMDgyODYwMSwiaWF0IjoxNzEwODI2ODAxLCJqdGkiOiIzNDRjODFiYy02YTQ2LTQxNGUtYjAwMS0wOGJjZDY5OGJiZDkiLCJhY2N0Ijoia29vQG1lZ2F6b25lLmNvbSIsInVzZXJuYW1lIjoia29vQG1lZ2F6b25lLmNvbSJ9.V1NJcxlMGmgP6flbU8325YyPHcGkqxPTFiuIqYy2OtoTYrzegquw9xlA-AeoLSTT4yWtc7BBQuRRtdMj-S153p8oSGvvuL52RWnvdUFj6vgB8sdR7yNOH4tXtpfSnd2fsa3WZcCVF9krT1kSc94jEXPoHqdusnkr0HsfzxrsdV5Arp3Uol5j2fYYJ52_x_fHNwIky4faFg7xGmjqhYmutf-hSq8fjUAhchM53Z9syM1Sb32LaNRJgYHs50XCgKWQO4GmnXxhMf1GDMjNXWhzl6rsOFuroFMQWSbVOqXImehVnMBRRKToO7TqK5hTQWAe5NfoAfsXhPyfCW9x8d1AoQ"



# 새로운 액세스 토큰 요청 함수
def refresh_access_token():
    url = "https://console.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "refresh_token": token_info["refresh_token"]
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        token_info["access_token"] = response.json()["access_token"]
        print("token재발급")
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_orgs', methods=['GET'])
def get_orgs():
    global token_info
    # VMware API 호출
    api_url = "https://vmc.vmware.com/vmc/api/orgs"
    headers = {
        "Content-Type": "application/json",
        "csp-auth-token": token_info["access_token"]
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 401:  # 토큰 만료 시
            if refresh_access_token():  # 토큰 갱신 시도
                # 갱신된 토큰으로 다시 요청 보내기
                headers["csp-auth-token"] = token_info["access_token"]
                response = requests.get(api_url, headers=headers)
            else:
                return jsonify({'error': 'Failed to refresh token'}), 401
        if response.status_code == 200:
            orgs_data = response.json()
            
            org_info = [{'display_name': org['display_name'], 'org_id': org['id']} for org in orgs_data]
            return jsonify({'org_info': org_info})
        else:
            return jsonify({'error': 'Failed to retrieve orgs'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# T0 라우팅 테이블 조회 엔드포인트
@app.route('/get_routing_tables', methods=['GET'])
def get_routing_tables():
    # 요청에서 sddc_id와 org_id 추출
    sddc_id = request.args.get('sddc_id')
    org_id = request.args.get('org_id')

    # VMware API 호출
    api_url = f"https://nsx-3-36-22-123.rp.vmwarevmc.com/vmc/reverse-proxy/api/orgs/{org_id}/sddcs/{sddc_id}/sks-nsxt-manager/policy/api/v1/infra/tier-0s/vmc/routing-table"
    headers = {
        "Content-Type": "application/json",
        "csp-auth-token": token_info["access_token"]
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 401:  # 토큰 만료 시
            if refresh_access_token():  # 토큰 갱신 시도
                # 갱신된 토큰으로 다시 요청 보내기
                headers["csp-auth-token"] = token_info["access_token"]
                response = requests.get(api_url, headers=headers)
            else:
                return jsonify({'error': 'Failed to refresh token'}), 401
        if response.status_code == 200:
            data = response.json()
            # 라우팅 테이블 정보 추출
            route_entries = data.get("results", [])[0].get("route_entries", [])
            # 추출된 정보 반환
            return jsonify(route_entries)
        else:
            return jsonify({'error': 'Failed to get routing tables'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_sddc_id', methods=['GET'])
def get_sddc_id():
    # 요청에서 org_id 추출
    org_id = request.args.get('org_id')
    print(org_id)
    # VMware API 호출
    api_url = f"https://vmc.vmware.com/vmc/api/orgs/{org_id}/sddcs"
    headers = {
        "Content-Type": "application/json",
        "csp-auth-token": token_info["access_token"]
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 401:  # 토큰 만료 시
            if refresh_access_token():  # 토큰 갱신 시도
                # 갱신된 토큰으로 다시 요청 보내기
                headers["csp-auth-token"] = token_info["access_token"]
                response = requests.get(api_url, headers=headers)
            else:
                return jsonify({'error': 'Failed to refresh token'}), 401
        if response.status_code == 200:
            data = response.json()
            print(data)
          
            # 첫 번째 SDDC의 ID 반환 (단일 SDDC 조회라고 가정)
            sddc_id = data[0]['id']
            print(sddc_id)
            return jsonify({'sddc_id': sddc_id})
        else:
            return jsonify({'error': 'Failed to get sddc_id'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)