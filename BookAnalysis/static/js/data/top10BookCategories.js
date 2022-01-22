// 实例化对象
const myChart = echarts.init(document.getElementById('top10BookCategories'));
// 指定配置和数据
myChart.setOption({
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    grid: {
        left: '2%',
        right: '2%',
        bottom: '2%',
        top: '5%',
        containLabel: true,
        // backgroundColor: #fff
    },
    xAxis: [
        {
            type: 'category',
            // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
                alignWithLabel: true
            },
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: "12"
                }
            },
            axisLine: {
                show: false
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: "12"
                }
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                    // width: 1,
                    // type: "solid"
                }
            },
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                }
            }
        }
    ],
    series: [
        {
            name: 'Direct',
            type: 'bar',
            barWidth: '60%',
            // data: [10, 52, 200, 334, 390, 330, 2200]
        }
    ]
});

const response = request({url: '/v1/data/top10BookCategories'})
response.then((res) => {
    myChart.setOption({
        xAxis: [{
            data: res['xAxis'],
        }],
        series: [{
            data: res['yAxis']
        }]
    });
})

window.addEventListener("resize", function () {
    myChart.resize();
});