These scripts import and execute function foo from [`A/B/__init__.py`](A/B/__init__.py)

<table>
<tr>
<th>script</th>
<th>import</th>
<th>call</th>
</tr>
<tr>
<td>d1_specific</td>
<td><code>from path.A.B import foo</code></td>
<td><code>foo()</code></td>
</tr>
<tr>
<td>d2_star</td>
<td><code>from path.A.B import *</code></td>
<td><code>foo()</code></td>
</tr>
<tr>
<td>d3_module_long</td>
<td><code>import path.A.B</code></td>
<td><code>path.A.B.foo()</code></td>
</tr>
<tr>
<td>d4_module_as</td>
<td><code>import path.A.B as B</code></td>
<td><code>B.foo()</code></td>
</tr>
</table>
