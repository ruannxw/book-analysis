(async () => {
    var res = await request({ url: '/v1/data/top10Authors' })
    // 实例化对象
    const top10Authors = echarts.init(document.getElementById('top10Authors'));

    // 指定配置和数据
    top10Authors.setOption({
        grid: {
            left: '2%',
            right: '2%',
            bottom: '2%',
            top: '20%',
            containLabel: true,
            // backgroundColor: #fff
        },
        xAxis: {
            data: res['xAxis'],
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            z: 10,
            name: '出版社名称',
            nameTextStyle: {
                // 坐标轴名称样式
                color: '#fff',
                padding: [5, 0, 0, -5]
            },
            // nameGap: 25, // 坐标轴名称与轴线之间的距离
            axisLabel: {
                // 坐标轴标签
                show: true, // 是否显示
                inside: false, // 是否朝内
                // rotate: 30, // 旋转角度
                // margin: 15, // 刻度标签与轴线之间的距离
                color: '#fff', // 默认取轴线的颜色
                textStyle: {
                    color: '#fff'
                },
                formatter: function (value) {
                    return value.length > 2 ? value.substring(0, 2) + '...' : value
                }
            }
        },
        yAxis: {
            name: '数量 单位:（本）',
            type: 'value',
            nameTextStyle: {
                // 坐标轴名称样式
                color: '#fff',
                padding: [0, 0, 0, 30] // 坐标轴名称相对位置
            },
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                textStyle: {
                    color: '#fff'
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
                name: '作品数量',
                type: 'bar',
                itemStyle: {
                    color: 'rgba(0,0,0,0.05)'
                },
                barGap: '-100%',
                barCategoryGap: '40%',
                animation: false
            },

            {
                type: 'bar',
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: '#83bff6' },
                        { offset: 0.5, color: '#188df0' },
                        { offset: 1, color: '#188df0' }
                    ])
                },
                emphasis: {
                    itemStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: '#2378f7' },
                            { offset: 0.7, color: '#2378f7' },
                            { offset: 1, color: '#83bff6' }
                        ])
                    }
                },
                data: res['yAxis']
            }
        ],
        tooltip: {
            trigger: 'axis', //坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
            axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
            }
        }
    });
})()


// window.addEventListener("resize", function () {
//     top10Authors.resize();
// });