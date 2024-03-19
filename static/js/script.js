function fetchRoutingtable() {
    // 입력된 sddc_id와 org_id 가져오기
    const sddc_id = document.getElementById('sddc_id').value;
    const org_id = document.getElementById('org_id').value;

    // GET 요청으로 클러스터 정보 가져오기
    fetch(`/get_routing_tables?sddc_id=${sddc_id}&org_id=${org_id}`)
        .then(response => response.json())
        .then(data => {
            const clusterResultDiv = document.getElementById('clusterResult');
            // 결과를 클러스터 결과 디브에 표시
            clusterResultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => console.error('Error fetching clusters:', error));
}

// 페이지 로드 시 클러스터 정보 가져오기
document.getElementById('clusterForm').addEventListener('submit', function(event) {
    event.preventDefault(); // 폼 기본 동작 방지
    fetchRoutingtable(); // 클러스터 정보 가져오기 호출
});