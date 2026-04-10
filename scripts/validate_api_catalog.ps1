$ErrorActionPreference = 'Stop'

$catalogPath = "c:\Users\chhed\Desktop\stan\stan-v1\data\api_catalog.json"
$outJson = "c:\Users\chhed\Desktop\stan\stan-v1\data\api_catalog_validation.json"
$outMd = "c:\Users\chhed\Desktop\stan\stan-v1\data\api_catalog_keep_remove.md"

$defaults = @{
  country='india'; postal_code='110001'; lat='19.0176'; lon='72.8562'; city='mumbai'
  query='python'; title='Python_(programming_language)'; text='hello'; from='USD'; to='INR'
  coin_id='bitcoin'; vs='usd'; word='good'; source='en'; target='es'; domain='example.com'
  url='https://example.com'; postcode='SW1A1AA'; cep='01001000'; year='2026'; icao='KMCI'
  box_id='57000b8745fd40c8196ad04c'; seed='stan'; status='200'; name='alex'; user_agent='Mozilla/5.0'
  size='32'; deck_count='1'; deck_id='new'; count='3'; entry='apple'; ifsc='YESB0DNB002'
  geo='usa'; industry='marketing'; amount='5'; max_price='15'; base='USD'; barcode='737628064502'
  make='merc'; namespace='stan'; key='hits'; intdes='2023-015'; start='2026-04-01'; end='2026-04-10'
  minmag='4.5'; timezone='UTC'; date='today'; package_id='5953da6b-d81b-4a2c-8b27-145892827fb0'
  dataset='erm2-nwe9'; query_string='$limit=1'; brand='maybelline'; mbid='5b11f4ce-a62d-471e-81fc-a69a8278c7da'
  genre='electro'; radical='85'; route='CR-Providence'; vehicle_id='BE.NMBS.IC1832'; paras='2'
  type='meat-and-filler'; page='1'; paragraphs='2'; number='42'; kind='math'; brand_id='59'
  isbn='9780525440987'; target_obj='J99TS7A'; operation='factor'; expression='x^2-1'
}

function Resolve-Template([string]$template) {
  [regex]::Replace($template, '\{([a-zA-Z0-9_]+)\}', {
    param($m)
    $k = $m.Groups[1].Value
    if ($defaults.ContainsKey($k)) {
      [uri]::EscapeDataString([string]$defaults[$k])
    } else {
      'test'
    }
  })
}

$catalog = Get-Content $catalogPath -Raw | ConvertFrom-Json
$results = @()

foreach ($item in $catalog) {
  $url = Resolve-Template([string]$item.url)
  $method = [string]$item.method
  $id = [string]$item.id
  $name = [string]$item.name
  $category = [string]$item.category

  $status = $null
  $ok = $false
  $errMsg = $null
  $preview = ''
  $ms = 0

  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  try {
    if ($method -eq 'GET') {
      $resp = Invoke-WebRequest -Uri $url -Method GET -TimeoutSec 12 -Headers @{'User-Agent'='Stan-Validator/1.0'} -UseBasicParsing -ErrorAction Stop
    } elseif ($method -eq 'POST_JSON') {
      $bodyObj = @{}
      if ($item.PSObject.Properties.Name -contains 'json_body' -and $null -ne $item.json_body) {
        $item.json_body.PSObject.Properties | ForEach-Object {
          $v = [string]$_.Value
          $filled = [regex]::Replace($v, '\{([a-zA-Z0-9_]+)\}', {
            param($m)
            $k = $m.Groups[1].Value
            if ($defaults.ContainsKey($k)) { [string]$defaults[$k] } else { 'test' }
          })
          $bodyObj[$_.Name] = $filled
        }
      }
      $json = $bodyObj | ConvertTo-Json -Compress
      $resp = Invoke-WebRequest -Uri $url -Method POST -TimeoutSec 12 -ContentType 'application/json' -Body $json -Headers @{'User-Agent'='Stan-Validator/1.0'} -UseBasicParsing -ErrorAction Stop
    } elseif ($method -eq 'POST_FORM') {
      $form = @{}
      if ($item.PSObject.Properties.Name -contains 'form_body' -and $null -ne $item.form_body) {
        $item.form_body.PSObject.Properties | ForEach-Object {
          $v = [string]$_.Value
          $filled = [regex]::Replace($v, '\{([a-zA-Z0-9_]+)\}', {
            param($m)
            $k = $m.Groups[1].Value
            if ($defaults.ContainsKey($k)) { [string]$defaults[$k] } else { 'test' }
          })
          $form[$_.Name] = $filled
        }
      }
      $resp = Invoke-WebRequest -Uri $url -Method POST -TimeoutSec 12 -Body $form -Headers @{'User-Agent'='Stan-Validator/1.0'} -UseBasicParsing -ErrorAction Stop
    } else {
      throw "Unsupported method: $method"
    }

    $status = [int]$resp.StatusCode
    $ok = ($status -ge 200 -and $status -lt 300)
    $preview = [string]$resp.Content
    if ($preview.Length -gt 160) { $preview = $preview.Substring(0, 160) }
  } catch {
    $ex = $_.Exception
    if ($ex.PSObject.Properties.Name -contains 'Response' -and $null -ne $ex.Response) {
      try { $status = [int]$ex.Response.StatusCode.value__ } catch {}
    }
    $errMsg = [string]$ex.Message
    if ($errMsg.Length -gt 220) { $errMsg = $errMsg.Substring(0, 220) }
  }

  $sw.Stop()
  $ms = [int]$sw.ElapsedMilliseconds

  $decision = 'review'
  if ($ok) {
    $decision = 'keep'
  } elseif ($null -ne $status -and ($status -eq 401 -or $status -eq 403 -or $status -eq 404 -or $status -eq 405 -or $status -eq 429)) {
    $decision = 'review'
  } elseif ($null -ne $status -and $status -ge 500) {
    $decision = 'remove'
  } elseif ($errMsg -match 'NameResolutionFailure|No such host|Unsupported method|Invalid URI|timed out|Unable to connect') {
    $decision = 'remove'
  }

  $results += [pscustomobject]@{
    id = $id
    name = $name
    category = $category
    method = $method
    url = $url
    status = $status
    ok = $ok
    latency_ms = $ms
    error = $errMsg
    preview = $preview
    decision = $decision
  }
}

$results | ConvertTo-Json -Depth 6 | Set-Content $outJson

$keep = $results | Where-Object decision -eq 'keep' | Sort-Object id
$review = $results | Where-Object decision -eq 'review' | Sort-Object id
$remove = $results | Where-Object decision -eq 'remove' | Sort-Object id

$lines = @()
$lines += '# API Catalog Validation Report'
$lines += ''
$lines += "- Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$lines += "- Total: $($results.Count)"
$lines += "- Keep: $($keep.Count)"
$lines += "- Review: $($review.Count)"
$lines += "- Remove: $($remove.Count)"
$lines += ''
$lines += '## Keep'
foreach ($r in $keep) {
  $lines += "- $($r.id) | $($r.method) | $($r.status) | $($r.latency_ms)ms"
}
$lines += ''
$lines += '## Review'
foreach ($r in $review) {
  $lines += "- $($r.id) | $($r.method) | status=$($r.status) | err=$($r.error)"
}
$lines += ''
$lines += '## Remove'
foreach ($r in $remove) {
  $lines += "- $($r.id) | $($r.method) | status=$($r.status) | err=$($r.error)"
}
$lines += ''
$lines += '## Notes'
$lines += '- Review means endpoint may still be useful but needs parameter, auth, user-agent, or rate-limit handling.'
$lines += '- Remove means consistently unhealthy in this sweep (server-side failure or unreachable).'

$lines | Set-Content $outMd
Write-Output "Validation complete: $($results.Count) APIs checked. Keep=$($keep.Count) Review=$($review.Count) Remove=$($remove.Count)"