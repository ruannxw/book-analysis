(async () => {
    var res = await request({ url: '/v1/data/everyMonthCommentNum' });
    var xAxisLabel = [];
    for (let i = 0; i < res['xAxis'].length; i++) {
        xAxisLabel.push(`${res['xAxis'][i]}月`)
    }
    // console.log(res['yAxis'], xAxisLabel)
    // 实例化对象
    const everyMonthCommentNum = echarts.init(document.getElementById('everyMonthCommentNum'));
    // 指定配置和数据
    everyMonthCommentNum.setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            left: '3%',
            right: '2%',
            bottom: '2%',
            top: '15%',
            containLabel: true,
            // backgroundColor: #fff
        },
        xAxis: {
            type: 'category',
            data: xAxisLabel,
            name: '时间',
            // offset: 25,
            axisLabel: {
                // interval: 0,
                // rotate: 40,
                align: 'center',
                textStyle: {
                    color: '#fff'
                },
            },
            grid: {
                left: '10%',
                bottom: '35%'
            },
            textStyle: {
                color: '#fff'
            },
        },
        yAxis: {
            name: '数量 单位: 万（本）',
            type: 'value',
            nameTextStyle: {
                // 坐标轴名称样式
                color: '#fff',
                padding: [0, 0, 0, 60] // 坐标轴名称相对位置
            },
            axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                formatter: function (value) {
                    if (value > 10000) {
                        return value / 10000 + 'w'
                    } else if (value > 0) {
                        return (value / 1000).toFixed(1) + 'k'
                    } else {
                        return value
                    }
                }
            }
        },
        dataZoom: [
            {
                type: 'inside'
            }
        ],
        series: [
            {
                data: res['yAxis'],
                type: 'line',
                smooth: true
            }
        ]
    });
})();