/*
JsUnit - a JUnit port for JavaScript
Copyright (C) 1999,2000,2001,2002,2003,2007 Joerg Schaible

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

/**
 * Some simple tests.
 */
function SimpleTest(name)
{
    TestCase.call( this, name );
}
function SimpleTest_setUp()
{
}
function SimpleTest_testIsFactor()
{
    this.assertTrue(isFactor(7, 1, 7));
    this.assertFalse(isFactor(7, 0, 7));
    this.assertFalse(isFactor(14, 7, 7));
}
function SimpleTest_testToBase()
{
    this.assertTrue(arrays_equal([0], toBase(0, 7)));
    this.assertTrue(arrays_equal([1], toBase(1, 7)));
    this.assertTrue(arrays_equal([0,1], toBase(7, 7)));
    this.assertTrue(arrays_equal([0,2], toBase(14, 7)));
    this.assertTrue(arrays_equal([0,0,1], toBase(49, 7)));
    this.assertTrue(arrays_equal([0,1,1], toBase(56, 7)));
    this.assertTrue(arrays_equal([1,1,1], toBase(57, 7)));
}
function arrays_equal(a,b) 
{
    if (a == null) return (b == null);
    if (a.length != b.length) return false;
    for (i = 0; i < a.length; i ++) {
	if (a[i] != b[i]) {
	    return false;
	}
    }
    return true;
}


SimpleTest.prototype = new TestCase();
SimpleTest.glue();

function SimpleTestSuite()
{
    TestSuite.call( this, "SimpleTestSuite" );
    this.addTestSuite( SimpleTest );
}
SimpleTestSuite.prototype = new TestSuite();
SimpleTestSuite.prototype.suite = function () { return new SimpleTestSuite(); }
