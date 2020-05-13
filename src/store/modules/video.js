
const state = {
    dataValue: null,
  	timeValue: null,
  	tableValue: [],
  	pictureValue: null,
	realVideoTimer: null,
	personalName: {
		information: '用户名：',
		content: '王小虎'
	},
	personalPhone: {
		information: '电话号码：',
		content: '王小虎'
	},
	personalCom: {
		information: '所属单位：',
		content: '王小虎'
	},
	personalSsl: {
		information: '宿舍楼号：',
		content: '王小虎'
	},
	personalSsh: {
		information: '宿舍号：',
		content: '王小虎'
	},
	personalEqu: {
		information: '设备编号：',
		content: '王小虎'
	}
}

const mutations = {
	setDataValue(state, DataValue){
		state.dataValue = DataValue;
	},
	setTimeValue(state, TimeValue){
		state.timeValue = TimeValue;
	},
	setTableValue(state, TableValue){
		state.tableValue = TableValue;
	},
	setPictureValue(state, PictureValue){
		state.pictureValue = PictureValue;
	},
	setRealVideoTimer(state, RealVideoTimer){
		state.realVideoTimer = RealVideoTimer;
	},
	setPersonalPhone(state, PersonalPhone){
		state.personalPhone.content = PersonalPhone;
	},
	setPersonalCom(state, PersonalCom){
		state.personalCom.content = PersonalCom;
	},
	setPersonalSsl(state, PersonalSsl){
		state.personalSsl.content = PersonalSsl;
	},
	setPersonalSsh(state, PersonalSsh){
		state.personalSsh.content = PersonalSsh;
	}
}

const getters = {
	getDataValue: state => {
		return state.dataValue;
	},
	getPersonalTab: state => {
		var personaltable = [state.personalName,state.personalPhone,state.personalCom
							 ,state.personalSsl,state.personalSsh,state.personalEqu];
		return personaltable;
	}
}


export default {
  namespaced: true,
  state,
  getters,
  mutations
}