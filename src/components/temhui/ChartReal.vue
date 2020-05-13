<template>
  <div id="chartElem">
      <highcharts class="chart" :options="chartOptions" :updateArgs="updateArgs"></highcharts>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: '',
      points: [10, 0, 8, 2, 6, 4, 5, 5],
      chartType: 'Spline',
      seriesColor: '#00a8e1',
      colorInputIsSupported: null,
      animationDuration: 1000,
      updateArgs: [true, true, {duration: 1000}],
      chartOptions: {
        chart: {
          type: 'spline'
        },
        title: {
          text: '实时温湿度'
        },
		xAxis:{
		   title:{
		       text:'时间'
		   }
		},
		yAxis: [{ // Primary yAxis
				labels: {
					format: '{value}°C',
				},
				title: {
					text: '温度',
				},
                plotLines:[{
                    color:'red',           //线的颜色，定义为红色
                    dashStyle:'solid',     //默认值，这里定义为实线
                    value:40,               //定义在那个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
                    width:2                //标示线的宽度，2px
                }]
			}, { // Secondary yAxis
				title: {
					text: '降雨量',
				},
				labels: {
					format: '{value} %RH',
				},
				opposite: true
		}],
		legend: {
				layout: 'vertical',
				align: 'left',
				x: 120,
				verticalAlign: 'top',
				y: 100,
				floating: true,
		},
        series: [
			{
				yAxis: 0,
				name: "温度",
				data:  [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
				color: '#3f8cfa',
				tooltip: {
				        valueSuffix: ' °C'
				}
			},
			{
				yAxis: 1,
				name: "湿度",
				data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
				color: '#fe377d',
				tooltip: {
				        valueSuffix: ' %RH'
				}
			}
		],
		tooltip: {
				xDateFormat: '%Y-%m-%d',
				shared: true,
				crosshairs: true,
                animation: true,               // 是否启用动画效果
                style: {                      // 文字内容相关样式
                    fontSize: "12px",
                    fontWeight: "blod",
                    fontFamily: "Courir new"
                }
		},
      }
    }
  },
  created () {
    let i = document.createElement('input')
    i.setAttribute('type', 'color');
    (i.type === 'color') ? this.colorInputIsSupported = true : this.colorInputIsSupported = false
  },
  watch: {
    title (newValue) {
      this.chartOptions.title.text = newValue
    },
    points (newValue) {
      this.chartOptions.series[0].data = newValue
    },
    chartType (newValue) {
      this.chartOptions.chart.type = newValue.toLowerCase()
    },
    seriesColor (newValue) {
      this.chartOptions.series[0].color = newValue.toLowerCase()
    },
    animationDuration (newValue) {
      this.updateArgs[2].duration = Number(newValue)
    }
  }
}
</script>

<style scoped>
input[type="color"]::-webkit-color-swatch-wrapper {
  padding: 0;
}
#colorPicker {
  border: 0;
  padding: 0;
  margin: 0;
  width: 30px;
  height: 30px;
}
.numberInput {
  width: 30px;
}
#chartElem{
	min-width:400px;
	height:400px;
}
</style>
