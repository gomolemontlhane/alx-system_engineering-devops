# Puppet manifest to execute a command to kill a process named killmenow

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin',
  refreshonly => true,
}
