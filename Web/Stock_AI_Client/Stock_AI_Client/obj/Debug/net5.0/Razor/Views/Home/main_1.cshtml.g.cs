#pragma checksum "C:\Users\hee05\OneDrive\바탕 화면\대학\캡스톤_지능_파일\Stock_AI_Client\Stock_AI_Client\Views\Home\main_1.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "a01fed58241d5adf3429327950b42b5d525a8ed6"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Home_main_1), @"mvc.1.0.view", @"/Views/Home/main_1.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "C:\Users\hee05\OneDrive\바탕 화면\대학\캡스톤_지능_파일\Stock_AI_Client\Stock_AI_Client\Views\_ViewImports.cshtml"
using Stock_AI_Client;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\hee05\OneDrive\바탕 화면\대학\캡스톤_지능_파일\Stock_AI_Client\Stock_AI_Client\Views\_ViewImports.cshtml"
using Stock_AI_Client.Models;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"a01fed58241d5adf3429327950b42b5d525a8ed6", @"/Views/Home/main_1.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"f7de834f45a35df8394c3f5f5116d89778ed00ad", @"/Views/_ViewImports.cshtml")]
    public class Views_Home_main_1 : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<dynamic>
    {
        #line hidden
        #pragma warning disable 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext __tagHelperExecutionContext;
        #pragma warning restore 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner __tagHelperRunner = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner();
        #pragma warning disable 0169
        private string __tagHelperStringValueBuffer;
        #pragma warning restore 0169
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __backed__tagHelperScopeManager = null;
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __tagHelperScopeManager
        {
            get
            {
                if (__backed__tagHelperScopeManager == null)
                {
                    __backed__tagHelperScopeManager = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager(StartTagHelperWritingScope, EndTagHelperWritingScope);
                }
                return __backed__tagHelperScopeManager;
            }
        }
        private global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.HeadTagHelper __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_HeadTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            WriteLiteral("<!DOCTYPE html>\r\n\r\n");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("head", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "a01fed58241d5adf3429327950b42b5d525a8ed63166", async() => {
                WriteLiteral("\r\n    <script src=\"https://code.jquery.com/jquery-3.1.1.min.js\"></script>\r\n    <script src=\"https://code.highcharts.com/stock/highstock.js\"></script>\r\n    <script src=\"https://code.highcharts.com/stock/modules/exporting.js\"></script>\r\n");
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_HeadTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.HeadTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_HeadTagHelper);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral(@"



<!-- Page Heading -->
<div class=""d-sm-flex align-items-center justify-content-between mb-4"">
    <h1 class=""h3 mb-0 text-gray-800"">AI 예측</h1>
    <i class=""fas fa-download fa-sm text-white-50""></i>
</div>


<div class=""modal-footer"">
    <button type=""button"" class=""btn btn-outline-primary"" onclick=""AITrain()"">학습하기</button>
    <button type=""button"" class=""btn btn-outline-primary"" style=""margin-right:89%"" onclick=""AIDisplay()"">예측하기</button>
</div>


");
            WriteLiteral(@"

<div class=""container-fluid"" style=""margin-top:30px;"">



    <!-- Content Row -->

    <div class=""row"">

        <!-- Area Chart -->
        <div class=""col-xl-12 col-lg-12"">
            <div class=""card shadow mb-4"">
                <!-- Card Header - Dropdown -->
                <div class=""card-header py-3 d-flex flex-row align-items-center justify-content-between"">
                    <h6 class=""m-0 font-weight-bold text-primary"">예측</h6>
                    <div class=""dropdown no-arrow"">
                        <a class=""dropdown-toggle"" href=""#"" role=""button"" id=""dropdownMenuLink""
                           data-toggle=""dropdown"" aria-haspopup=""true"" aria-expanded=""false"">
                            <i class=""fas fa-ellipsis-v fa-sm fa-fw text-gray-400""></i>
                        </a>
                        <div class=""dropdown-menu dropdown-menu-right shadow animated--fade-in""
                             aria-labelledby=""dropdownMenuLink"">
                            <di");
            WriteLiteral(@"v class=""dropdown-header"">Dropdown Header:</div>
                            <a class=""dropdown-item"" href=""#"">Action</a>
                            <a class=""dropdown-item"" href=""#"">Another action</a>
                            <div class=""dropdown-divider""></div>
                            <a class=""dropdown-item"" href=""#"">Something else here</a>
                        </div>
                    </div>
                </div>
                <!-- Card Body -->
                <div class=""card-body"">
                    <div class=""chart-area"">
                        <canvas id=""myAreaChart_AI""></canvas>
                    </div>
                </div>
            </div>
        </div>

    </div>

</div>

<div class=""container-fluid"">



    <!-- Content Row -->

    <div class=""row"">

        <!-- Area Chart -->
        <div class=""col-xl-12 col-lg-12"">
            <div class=""card shadow mb-4"">
                <!-- Card Header - Dropdown -->
                <div class");
            WriteLiteral(@"=""card-header py-3 d-flex flex-row align-items-center justify-content-between"">
                    <h6 class=""m-0 font-weight-bold text-primary"">예측 VS 실제</h6>
                    <div class=""dropdown no-arrow"">
                        <a class=""dropdown-toggle"" href=""#"" role=""button"" id=""dropdownMenuLink""
                           data-toggle=""dropdown"" aria-haspopup=""true"" aria-expanded=""false"">
                            <i class=""fas fa-ellipsis-v fa-sm fa-fw text-gray-400""></i>
                        </a>
                        <div class=""dropdown-menu dropdown-menu-right shadow animated--fade-in""
                             aria-labelledby=""dropdownMenuLink"">
                            <div class=""dropdown-header"">Dropdown Header:</div>
                            <a class=""dropdown-item"" href=""#"">Action</a>
                            <a class=""dropdown-item"" href=""#"">Another action</a>
                            <div class=""dropdown-divider""></div>
                            <a c");
            WriteLiteral(@"lass=""dropdown-item"" href=""#"">Something else here</a>
                        </div>
                    </div>
                </div>
                <!-- Card Body -->
                <div class=""card-body"">
                    <div class=""chart-area"">
                        <canvas id=""myAreaChart""></canvas>
                    </div>
                </div>
            </div>
        </div>

    </div>

</div>


<script>



    function AITrain() {

        console.log(""학습하기"");

    }

    function AIDisplay() {

        console.log(""예측하기"");

    }


    //function insertItem() {

    //    console.log(""insetItem 함수 초훌"")
    //    let name = {
    //        ""name"": $(""#search_name"").val()
    //    };

    //    Item(name);
    //}
    //function Item(name) {		// 추가

    //    console.log('item 함수 호출');
    //    console.log(name);

    //    fetch(""http://localhost:5000"" + ""/asd"", {
    //        method: 'POST',
    //        headers: {
    //          ");
            WriteLiteral(@"  'Accept': 'application/json',
    //            'Content-Type': 'application/json',
    //        },
    //        body: JSON.stringify(name)

    //    })

    //        .then((res) => {    
    //            if (res.ok) {
    //                console.log(res.json);
    //            }
    //            else {  
    //                alert('오류가 발생했습니다.');
    //                console.error(res);
    //            }
    //        }).catch(err => console.error(err))
    //        .then(data => console.log(data))
    //}

</script>
");
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<dynamic> Html { get; private set; }
    }
}
#pragma warning restore 1591
