let modelData = null;
const $ = (id) => document.getElementById(id);

function treePredict(tree, row) {
  let node = 0;
  while (tree.feature[node] >= 0) {
    const featureIndex = tree.feature[node];
    node = row[featureIndex] <= tree.threshold[node] ? tree.left[node] : tree.right[node];
  }
  return tree.value[node];
}
function predictScore(values) {
  const row = modelData.features.map((key) => Number.isFinite(values[key]) ? values[key] : modelData.medians[key]);
  const total = modelData.forest.reduce((sum, tree) => sum + treePredict(tree, row), 0);
  return Math.max(0, Math.min(100, total / modelData.forest.length));
}
function showError(message) {
  const el = $('error-message'); el.textContent = message; el.hidden = false;
}
function clearError() { $('error-message').hidden = true; }
function renderResult(score, values) {
  const rounded = score.toFixed(1);
  $('result-content').innerHTML = `
    <div class="score-row"><div><div class="score-number">${rounded}<small>/100</small></div><div class="score-caption">Predicted exam score</div></div><div class="score-badge">AI estimate</div></div>
    <div class="meter" role="progressbar" aria-label="Predicted score" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${rounded}"><div style="width:${rounded}%"></div></div>
    <div class="meter-labels"><span>0</span><span>50</span><span>100</span></div>
    <div class="result-grid"><div><span>Study</span><b>${values.study_hours} h/day</b></div><div><span>Attendance</span><b>${values.attendance_percent}%</b></div><div><span>Previous score</span><b>${values.previous_score}/100</b></div><div><span>Sleep</span><b>${values.sleep_hours} h/day</b></div></div>
    <div class="insight"><span>✦</span><div><b>Prediction generated</b><p>This is a model-based estimate, not a guaranteed exam result.</p></div></div>`;
}
function setupChart(points) {
  const canvas = $('scoreChart');
  if (!canvas || !window.Chart || !points.length) {
    if (!window.Chart) $('chart-wrap').innerHTML = '<p class="chart-description">Chart library unavailable. The score predictor still works.</p>';
    return;
  }
  new Chart(canvas, {type:'scatter',data:{datasets:[{label:'Students',data:points,backgroundColor:'rgba(16,185,129,.65)',borderColor:'#10b981',pointRadius:4}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>`Study: ${c.raw.x}h · Score: ${c.raw.y}`}}},scales:{x:{title:{display:true,text:'Study hours per day'},min:0,grid:{color:'#eef2f7'}},y:{title:{display:true,text:'Exam score'},min:0,max:100,grid:{color:'#eef2f7'}}}}});
}
async function init() {
  try {
    const response = await fetch('./model.json');
    if (!response.ok) throw new Error('Could not load model.json');
    modelData = await response.json();
    $('metric-rows').textContent = modelData.metrics.rows;
    $('metric-mae').textContent = modelData.metrics.mae;
    $('metric-r2').textContent = modelData.metrics.r2;
    setupChart(modelData.chartData);
  } catch (error) {
    showError('The prediction model could not load. Make sure index.html and model.json are both published at the repository root.');
    console.error(error);
  }
}
$('predict-form').addEventListener('submit', (event) => {
  event.preventDefault(); clearError();
  if (!modelData) { showError('The model is still loading. Please wait a moment and try again.'); return; }
  const values = {
    study_hours: Number($('study_hours').value),
    attendance_percent: Number($('attendance_percent').value),
    previous_score: Number($('previous_score').value),
    sleep_hours: Number($('sleep_hours').value)
  };
  const specs = [
    ['study_hours',0,24,'Study hours'],['attendance_percent',0,100,'Attendance'],
    ['previous_score',0,100,'Previous score'],['sleep_hours',0,24,'Sleep hours']
  ];
  for (const [key,min,max,label] of specs) {
    if (!Number.isFinite(values[key]) || values[key] < min || values[key] > max) {
      showError(`${label} must be a number between ${min} and ${max}.`); $(key).focus(); return;
    }
  }
  renderResult(predictScore(values), values);
});
init();
