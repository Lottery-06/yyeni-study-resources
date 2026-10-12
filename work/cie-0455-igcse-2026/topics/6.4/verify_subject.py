"""Run the unchanged CLI checks, routing previous topics' generated files into 6.4.

Only write destinations are redirected; every check uses the real topic inputs.
"""
import sys
sys.dont_write_bytecode=True
import builtins,json,pathlib,runpy,subprocess,hashlib
ws=pathlib.Path('work/cie-0455-igcse-2026');td=ws/'topics/6.4';vd=td/'subject-validation'
if len(sys.argv)>1:
 t=sys.argv[1];actual=(ws/'topics'/t).resolve();dest=(vd/('topic-'+t.replace('.','-'))).resolve();dest.mkdir(parents=True,exist_ok=True)
 original_open=builtins.open
 def redirected_open(file,mode='r',*args,**kwargs):
  if isinstance(file,(str,pathlib.Path)) and any(m in mode for m in 'wax+'):
   p=pathlib.Path(file).resolve()
   if p.parent==actual and p.name in ('packet.sha256','packet.sha256.hash'):
    file=dest/p.name
  return original_open(file,mode,*args,**kwargs)
 builtins.open=redirected_open
 sys.argv=['standard/v0.2.0-draft/checks/run_checks.py',str(ws),t,'--out',str(dest/'qa_report.json')]
 runpy.run_path(sys.argv[0],run_name='__main__')
else:
 vd.mkdir(parents=True,exist_ok=True)
 rows=[]
 for d in sorted((ws/'topics').iterdir(),key=lambda p:[int(n) for n in p.name.split('.')]):
  if not d.is_dir():continue
  t=d.name
  if t=='6.4':
   proc=subprocess.run([sys.executable,'standard/v0.2.0-draft/checks/run_checks.py',str(ws),t],capture_output=True,text=True)
   report=d/'qa_report.json'
  else:
   proc=subprocess.run([sys.executable,__file__,t],capture_output=True,text=True)
   report=vd/('topic-'+t.replace('.','-'))/'qa_report.json'
  if not report.exists():print(proc.stdout,proc.stderr);raise SystemExit('Missing check report '+t)
  r=json.loads(report.read_text());fails=[c for c in r['deterministic_checks'] if c['status']=='fail']
  print(t+': '+r['release_decision'].upper()+' ('+str(len(fails))+' failures)',flush=True)
  for c in fails:print(c['check_id'],c['message'],flush=True)
  row={'topic_id':t,**r['metrics'],'release_decision':r['release_decision'],'failures':fails}
  rows.append(row)
 summary={'topics':rows,'totals':{k:sum(r[k] for r in rows) for k in ['claim_count','content_unit_count','learning_item_count','word_count']},'all_publish':all(r['release_decision']=='publish' for r in rows)}
 (vd/'summary.json').write_text(json.dumps(summary,indent=1)+'\n')
 print(json.dumps(summary['totals']))
 if not summary['all_publish']:raise SystemExit(1)
